import customtkinter

class game(customtkinter.CTkFrame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        
        # Example content for Scene 1
        label = customtkinter.CTkLabel(self, text="This is Game", font=("Arial", 24))
        label.pack(pady=50)

        button = customtkinter.CTkButton(self, text="Go to Game Over", command=lambda: manager.show_scene("Game Over"))
        button.pack(pady=20)

        button = customtkinter.CTkButton(self, text="Go to Home", command=lambda: manager.show_scene("Home"))
        button.pack(pady=0)
