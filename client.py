import socket 
# Create socket object 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# Connect to server 
host = '127.0.0.1' 
port = 5000 
client_socket.connect((host, port)) 
while True: 
    message = input("Enter message: ") 
    client_socket.send(message.encode()) 
    if message.lower() == 'exit': 
        break 
# Receive echoed message 
data = client_socket.recv(1024).decode() 
print("Server echoed:", data)
client_socket.close() 