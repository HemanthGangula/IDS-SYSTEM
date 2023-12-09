import os
import time
from collections import defaultdict
from scapy.all import *
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression  
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
training_data = pd.read_csv("ajay.csv")

# Assuming the target column is named "target" (adjust as per your data)
X_train = training_data.drop(columns=["target"])
y_train = training_data["target"]

# Train your Random Forest Classifier
clf1 = RandomForestClassifier()
clf1.fit(X_train, y_train)
def my_classification_predict(test_df):
    # Assuming the target column is named "target" (adjust as per your data)
    # Make sure to drop any columns that were not used during training
    X_test = test_df

    # Perform one-hot encoding on the categorical features, if needed
    X_test_encoded = pd.get_dummies(X_test)

    # Ensure that the columns in X_test_encoded are in the same order as X_train_encoded
    X_test_encoded = X_test_encoded.reindex(columns=X_train.columns, fill_value=0)

    # Make predictions using the pre-trained Random Forest Classifier
    y_pred = clf1.predict(X_test_encoded)

    return y_pred

# Example usage:
# Assuming you have a test dataframe named "test_data"
# predictions = my_classification_predict(test_data)

df_columns = ["SPort", "DPort", "SPkts", "DPkts", "SBytes", "DBytes", "Protocol", "SYN", "ACK", "FIN", "PSH", "RST", "URG",
              "SYN+ACK", "Duration", "IsAlive", "Service", "UniqueDests", "UniqueSrcs", "UniqueDestSocks", "UniqueSrcSocks"]
df = pd.DataFrame(columns=df_columns)

INTERVAL = 2  # 2 seconds interval

sessions = {}  # Store session information in a dictionary
unique_dests_for_src = defaultdict(set)
unique_srcs_for_dests = defaultdict(set)
unique_sock_dests_for_src = defaultdict(set)
unique_sock_srcs_for_dests = defaultdict(set)

# Function to handle each captured packet
def receive_packet(packet):
    if IP in packet:
        ip_packet = packet[IP]

        src_ip = ip_packet.src
        dest_ip = ip_packet.dst
        src_port = ip_packet.sport
        dest_port = ip_packet.dport

        protocol = ip_packet.proto  # IP protocol number

        session_key = (src_ip, src_port, dest_ip, dest_port, protocol)

        if session_key in sessions:
            session = sessions[session_key]
        else:
            session = {
                'src_IP': src_ip,
                'dest_IP': dest_ip,
                'src_port': src_port,
                'dest_port': dest_port,
                'protocol': protocol,
                'src_bytes': 0,
                'src_Pkts': 0,
                'ACK': 0,
                'SYN': 0,
                'FIN': 0,
                'PSH': 0,
                'RST': 0,
                'URG': 0,
                'SYN_ACK': 0,
                'isAlive': 1,
                'start_time': time.time(),
            }

        session['src_bytes'] += len(packet)
        session['src_Pkts'] += 1

        if TCP in packet:
            tcp_packet = packet[TCP]

            if tcp_packet.ack:
                session['ACK'] += 1
            if tcp_packet.flags & 2:  # SYN flag
                session['SYN'] += 1
            if tcp_packet.flags & 1:  # FIN flag
                session['FIN'] += 1
            if tcp_packet.flags & 8:  # PSH flag
                session['PSH'] += 1
            if tcp_packet.flags & 4:  # RST flag
                session['RST'] += 1
            if tcp_packet.flags & 32:  # URG flag
                session['URG'] += 1
            if tcp_packet.flags & 18:  # SYN and ACK flags
                session['SYN_ACK'] += 1

        sessions[session_key] = session

# Function to push session data to a file
def push_to_file():
    global sessions, unique_dests_for_src, unique_srcs_for_dests, unique_sock_dests_for_src, unique_sock_srcs_for_dests,df

    # Update duration information for live sessions
    current_time = time.time()
    for session_key, session in list(sessions.items()):  # Convert to list to avoid dict size changing during iteration
        if session['isAlive'] == 1:
            session['duration'] = current_time - session['start_time']
        else:
            del sessions[session_key]  # Remove finished sessions

    with open('output1.txt', 'a') as outfile:
        for session_key, session in sessions.items():
            src_ip, src_port, dest_ip, dest_port, protocol = session_key

            # Update unique destination IPs for the given source IP
            unique_dests_for_src[src_ip].add(dest_ip)

            # Update unique source IPs for the given destination IP
            unique_srcs_for_dests[dest_ip].add(src_ip)

            # Update unique destination sockets for the given source socket
            src_socket = f"{src_ip}:{src_port}"
            dest_socket = f"{dest_ip}:{dest_port}"
            unique_sock_dests_for_src[src_socket].add(dest_socket)

            # Update unique source sockets for the given destination socket
            unique_sock_srcs_for_dests[dest_socket].add(src_socket)

            ses_info = f"{src_port}, {dest_port}, {session['src_Pkts']}, 0, {session['src_bytes']}, 0, {protocol}, {session['SYN']}, {session['ACK']}, {session['FIN']}, {session['PSH']}, {session['RST']}, {session['URG']}, {session['SYN_ACK']}, {session['duration']}, {session['isAlive']}, 0, {len(unique_dests_for_src[src_ip])}, {len(unique_srcs_for_dests[dest_ip])}, {len(unique_sock_dests_for_src[src_socket])}, {len(unique_sock_srcs_for_dests[dest_socket])}"
            outfile.write(ses_info + '\n')
            ses_info_dict = {
                'SPort': src_port,
                'DPort': dest_port,
                'SPkts': session['src_Pkts'],
                'DPkts': 0,
                'SBytes': session['src_bytes'],
                'DBytes': 0,
                'Protocol': protocol,
                'SYN': session['SYN'],
                'ACK': session['ACK'],
                'FIN': session['FIN'],
                'PSH': session['PSH'],
                'RST': session['RST'],
                'URG': session['URG'],
                'SYN+ACK': session['SYN_ACK'],
                'Duration': session['duration'],
                'IsAlive': session['isAlive'],
                'Service': 0,
                'UniqueDests': len(unique_dests_for_src[src_ip]),
                'UniqueSrcs': len(unique_srcs_for_dests[dest_ip]),
                'UniqueDestSocks': len(unique_sock_dests_for_src[src_socket]),
                'UniqueSrcSocks': len(unique_sock_srcs_for_dests[dest_socket]),
            }
            df=pd.DataFrame([ses_info_dict]).reset_index(drop=True)
         
             
            print(df)
	 
            # Append the dictionary to the DataFrame
            predition=my_classification_predict(df)
            print(predition)

# Main function
if __name__ == '__main__':
    print("Interfaces available in the system:")
    interfaces = get_if_list()

    for i, interface in enumerate(interfaces):
        print(f"{i}: {interface}")

    dev = int(input("Select interface to start capturing: "))
    fname = input("Enter output file name: ")

    print(f"Capturing from interface: {interfaces[dev]} and outputting to {fname}")

    with open('output1.txt', 'w') as outfile:  # Open the file for writing (creates or truncates the file)
        header = "SPort, DPort, SPkts, DPkts, SBytes, DBytes, Protocol, SYN, ACK, FIN, PSH, RST, URG, SYN+ACK, Duration, IsAlive, Service, UniqueDests, UniqueSrcs, UniqueDestSocks, UniqueSrcSocks"
        outfile.write(header + '\n')

    while True:
        sniff(
            iface=interfaces[dev],
            prn=receive_packet,
            store=0,
            timeout=INTERVAL,
            count=0,
        )
        push_to_file()
