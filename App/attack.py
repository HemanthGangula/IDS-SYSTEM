import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the receiver's address and port (System2)
receiver_address = ('10.0.2.15', 12345)

# Connect to the receiver (System2)
s.connect(receiver_address)

# Specify the path to the .txt file you want to send
file_path = '/home/batman/neptune.txt'

# Open and read the .txt file
with open(file_path, 'rb') as file:
    file_data = file.read()

# Send the file data
s.sendall(file_data)

# Close the socket
s.close()
