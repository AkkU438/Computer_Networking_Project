import socket

# Server setup
HOST = "127.0.0.1"
PORT = 12345


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((HOST, PORT))
    print(f"Server running on {HOST}:{PORT}")

    players = []
    roles = {0: "Player 1", 1: "Player 2"}

    while len(players) < 2:
        data, addr = server_socket.recvfrom(1024)
        if addr not in players:
            players.append(addr)
            server_socket.sendto(roles[len(players) - 1].encode(), addr)
            print(f"{roles[len(players) - 1]} connected: {addr}")

    print("Both players connected. Relaying messages...")

    while True:
        try:
            data, addr = server_socket.recvfrom(1024)
            print(f"Received from {addr}: {data.decode()}")

            # Relay message to the other player
            other_player = players[1] if addr == players[0] else players[0]
            server_socket.sendto(data, other_player)
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
