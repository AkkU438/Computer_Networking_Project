import customtkinter

class game(customtkinter.CTkFrame):
    def __init__(self, parent, manager, client):
        super().__init__(parent)
        self.client = client  # Store client instance

        self.connect_to_server()
        
        label = customtkinter.CTkLabel(self, text="This is the Game", font=("Arial", 24))
        label.pack(pady=50)

        # Button to simulate a win event and send a message to the server
        button = customtkinter.CTkButton(self, text="Press to win", command=self.send_win_message)
        button.pack(pady=20)

        # Button to go back to the Home scene
        button = customtkinter.CTkButton(self, text="Go to Home", command=lambda: manager.show_scene("Home"))
        button.pack(pady=0)

    def connect_to_server(self):
        try:
            message = "Player has entered the Game scene."
            print(f"Connecting to server: {message}")
            self.client.send_message(message)
        except Exception as e:
            print(f"Error connecting to server: {e}")

    def send_win_message(self):
        try:
            message = "Player has won!"
            print(f"Sending win message: {message}")
            self.client.send_message(message)
        except Exception as e:
            print(f"Error sending win message: {e}")
