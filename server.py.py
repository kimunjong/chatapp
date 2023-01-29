import socket

server = socket.socket()
#by default ipv4 and TCP

server_ip = socket.gethostname()
server_port = 60611

server.bind( (server_ip, server_port) )
#we are binding our server to listen on specific ip and port

server.listen()

# server.listen(5) 5 client at a time

print(f"Server is Running on {server_ip}:{server_port}")

client, addr = server.accept()
# addr = (client_ip, client_port)
client_ip, client_port = addr
print("Dot A Connection froom Client")

print(f"Client Address is {client_ip}:{client_port}")

request = client.recv(1024).decode()
# no of bytes to recv from client

# we got bytes from network decode converting byte into string

print("\n\nClient's Request: ", request)

msg = input("Messege to Send: ").encode()
# input is always a string but we need bytes to send
#encode just converting string into bytes

client.send(msg)

client.close()

server.close()

#"server.py" [new] 42, 947c written

