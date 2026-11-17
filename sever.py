import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = '127.0.0.1' 
port = 5000 
server_socket.bind((host, port))
server_socket.listen(1) 
print("Echo Server is waiting for connection...") 
# Accept client connection 
client_socket, addr = server_socket.accept() 
print("Connected to:", addr) 
while True: 
    data = client_socket.recv(1024).decode() 
    if not data: 
        break 
print("Client:", data) 
# Send same message back to client 
client_socket.send(data.encode()) 
client_socket.close() 
server_socket.close() 