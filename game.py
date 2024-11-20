import customtkinter

class game(customtkinter.CTkFrame):
    def __init__(self, parent, manager, client):
        super().__init__(parent)
        self.client = client  # Store client instance
        
        label = customtkinter.CTkLabel(self, text="This is Game", font=("Arial", 24))
        label.pack(pady=50)

        # Button to simulate a win event and send a message to the server
        button = customtkinter.CTkButton(self, text="Press to win", command=self.send_win_message)
        button.pack(pady=20)

        # Button to go back to the Home scene
        button = customtkinter.CTkButton(self, text="Go to Home", command=lambda: manager.show_scene("Home"))
        button.pack(pady=0)

    def send_win_message(self):
        # Send a message to the server indicating the player won
        self.client.send_message("Player has won!")
