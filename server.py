import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('127.0.0.1', 65432)
    server_socket.bind(server_address)
    #server_socket.listen(1)
    print("Server is listening on port 65432...")
    
    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Recieved from {addr}: {data.decode()}")
        server_socket.sendto(b"Message received!", addr)

if __name__ == "__main__":
    start_server()
