import socket
import time

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Get destination IP and port from user
dest_ip = input("Enter destination IP: ")
dest_port = int(input("Enter destination port: "))

# Get packet data from user
packet_data = input("Enter packet data: ")

# Convert packet data to bytes
packet_data = packet_data.encode()

# Loop to send packets continuously
while True:
    # Send packet
    s.sendto(packet_data, (dest_ip, dest_port))

    # Sleep for 1 second
    time.sleep(1)

# Close socket
s.close()
