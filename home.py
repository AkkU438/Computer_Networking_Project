import customtkinter

class home(customtkinter.CTkFrame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        
        # Example content for Scene 2
        label = customtkinter.CTkLabel(self, text="This Home", font=("Arial", 24))
        label.pack(pady=50)

        button = customtkinter.CTkButton(self, text="Go to Game", command=lambda: manager.show_scene("Game"))
        button.pack(pady=20)
