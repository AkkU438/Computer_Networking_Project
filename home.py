import customtkinter

class home(customtkinter.CTkFrame):
    def __init__(self, parent, manager, client):
        super().__init__(parent)
        self.client = client  # Store client instance
        
        label = customtkinter.CTkLabel(self, text="This is Home", font=("Arial", 24))
        label.pack(pady=50)

        # Button to navigate to the Game scene
        button = customtkinter.CTkButton(self, text="Go to Game", command=lambda: manager.show_scene("Game"))
        button.pack(pady=20)
