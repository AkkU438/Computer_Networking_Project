import customtkinter

class gameOver(customtkinter.CTkFrame):
    def __init__(self, parent, manager, client):
        super().__init__(parent)
        self.client = client  # Store client instance
        
        label = customtkinter.CTkLabel(self, text="You win", font=("Arial", 24))
        label.pack(pady=50)

        # Button to go back to the Home scene
        button = customtkinter.CTkButton(self, text="Go to Home", command=lambda: manager.show_scene("Home"))
        button.pack(pady=20)
