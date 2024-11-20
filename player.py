import socket
import customtkinter
from SceneManager import SceneManager  # Import SceneManager to handle scenes

class UDPClient:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create UDP socket
    
    def send_message(self, message):
        """Send message to the server."""
        self.sock.sendto(message.encode(), (self.server_ip, self.server_port))

    def receive_message(self):
        """Receive message from the server."""
        data, _ = self.sock.recvfrom(1024)
        return data.decode()

    def close(self):
        """Close the socket."""
        self.sock.close()


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
        self.scenes[name].pack(fill="both", expand=True)


# Game class with UDP Client integration (example)
class game(customtkinter.CTkFrame):
    def __init__(self, parent, manager, client):
        super().__init__(parent)
        self.client = client  # Store client instance
        
        label = customtkinter.CTkLabel(self, text="This is Game", font=("Arial", 24))
        label.pack(pady=50)

        button = customtkinter.CTkButton(self, text="Press to win", command=self.send_win_message)
        button.pack(pady=20)

        button = customtkinter.CTkButton(self, text="Go to Home", command=lambda: manager.show_scene("Home"))
        button.pack(pady=0)

    def send_win_message(self):
        # Send a message to the server indicating the player won
        self.client.send_message("Player has won!")


# Game Over class (example)
class gameOver(customtkinter.CTkFrame):
    def __init__(self, parent, manager, client):
        super().__init__(parent)
        self.client = client  # Store client instance
        
        label = customtkinter.CTkLabel(self, text="You win", font=("Arial", 24))
        label.pack(pady=50)

        button = customtkinter.CTkButton(self, text="Go to Home", command=lambda: manager.show_scene("Home"))
        button.pack(pady=20)


# Home class (example)
class home(customtkinter.CTkFrame):
    def __init__(self, parent, manager, client):
        super().__init__(parent)
        self.client = client  # Store client instance
        
        label = customtkinter.CTkLabel(self, text="This is Home", font=("Arial", 24))
        label.pack(pady=50)

        button = customtkinter.CTkButton(self, text="Go to Game", command=lambda: manager.show_scene("Game"))
        button.pack(pady=20)


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
