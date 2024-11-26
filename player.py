import socket
import customtkinter
from SceneManager import SceneManager  # Import SceneManager to handle scenes
from game import FlashcardGame
from gameOver import gameOver
from home import home

class UDPClient:
    def __init__(self):
        self.server_ip = '127.0.0.1'
        self.server_port = 12345
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create UDP socket
    
    def send_message(self, message):
        """Send message to the server."""
        self.socket.sendto(message.encode(), (self.server_ip, self.server_port))

    def receive_message(self):
        """Receive message from the server."""
        data, _ = self.socket.recvfrom(1024)
        return data.decode()

    def close(self):
        """Close the socket."""
        self.socket.close()

