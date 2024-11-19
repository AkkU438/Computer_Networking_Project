import customtkinter
from game import game
from gameOver import gameOver
from home import home

class SceneManager(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Scene Manager")
        self.geometry("800x600")
        
        # Dictionary to store scenes
        self.scenes = {}

        # Add scenes to the manager
        self.add_scene("Game", game(self, self))
        self.add_scene("Game Over", gameOver(self, self))
        self.add_scene("Home", home(self,self))

        # Show the initial scene
        self.show_scene("Home")
    
    def add_scene(self, name, scene):
        """Add a scene to the manager."""
        self.scenes[name] = scene
    
    def show_scene(self, name):
        """Show a specific scene."""
        for scene in self.scenes.values():
            scene.pack_forget()
        self.scenes[name].pack(fill="both", expand=True)
