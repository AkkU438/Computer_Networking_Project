import customtkinter
from game import FlashcardGame
from gameOver import gameOver
from home import home
from GUIConfig import GUIConfig
from loginGUI import loginGUI
from player import UDPClient
from studyMat import FlashcardApp


class SceneManager(customtkinter.CTk):
    def __init__(self, client):
        super().__init__()
        self.title("Scene Manager")
        
        self.client = client  # Store the client object for scene access

        # Add scenes and pass the client object to each scene
        self.scenes = {}
        self.add_scene("Game", FlashcardGame(self, self, client))
        self.add_scene("Game Over", gameOver(self, self, client))
        self.add_scene("Home", home(self, self, client))
        self.add_scene("GUI_Config", GUIConfig(self,self,client))
        self.add_scene("Login_Config", loginGUI(self,self,client))
        self.add_scene("Player", UDPClient(self,self,client))
        self.add_scene("StudyMats", FlashcardApp(self,self,client))
        

        self.show_scene("Home")
    
    def add_scene(self, name, scene):
        """Add a scene to the manager."""
        self.scenes[name] = scene
    
    def show_scene(self, name):
        """Show a specific scene."""
        for scene in self.scenes.values():
            scene.pack_forget()
        self.scenes[name].pack(fill="both", expand=True)
