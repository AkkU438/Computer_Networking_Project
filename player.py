import socket
import customtkinter
from SceneManager import SceneManager  # Import SceneManager to handle scenes
from game import game
from gameOver import gameOver
from home import home

class UDPClient:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
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


class PlayerApp(customtkinter.CTk):
    def __init__(self, client):
        super().__init__()
        self.client = client  # Store the UDPClient instance
        self.title("Player App")
        self.geometry("800x600")
        
        self.scenes = {}

        # Initialize the scenes with the manager and pass the client instance
        self.add_scene("Game", game(self, self, client))
        self.add_scene("Game Over", gameOver(self, self, client))
        self.add_scene("Home", home(self, self, client))

        self.show_scene("Home")
    
    def add_scene(self, name, scene):
        """Add a scene to the manager."""
        self.scenes[name] = scene
    
    def show_scene(self, name):
        """Show a specific scene."""
        for scene in self.scenes.values():
            scene.pack_forget()
        if name == "Game" and hasattr(self.scenes[name], "connect_to_server"):
            self.scenes[name].connect_to_server()
        self.scenes[name].pack(fill="both", expand=True)

def main():
    # Initialize UDP client with server IP and port
    client = UDPClient(server_ip="127.0.0.1", server_port=12345)  # Update with appropriate IP and port

    # Launch the application with the client instance
    app = PlayerApp(client)
    app.mainloop()

    # Close the client after the app finishes
    client.close()


if __name__ == "__main__":
    main()
