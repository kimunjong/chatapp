import socket

client = socket.socket()
# default tcp and ipv4 socket

server_ip = "13.233.194.196"
server_port = 60611

client.connect( (server_ip, server_port) )

print(f"Connected to server at {server_ip}:{server_port}")

request = input("Mesage to Send: ").encode()

client.send(request)

response = client.recv(1024).decode()

# decode bytes -> string

print("Response: ", response)

client.close()