from PIL import Image, ImageTk
import customtkinter
from GUIConfig import GUIConfig
import json

class home(GUIConfig):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        """ #Standardized window size + grid: 28 columns (0-27) and 20 rows (0-19)
        self.title("home")
        self.geometry("1050x750") #window size
        self.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27), weight=1)
        self.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19), weight=1)
        #Adds logo to top left corner
        logo_path = "StudyBat Logo.png"
        logo = Image.open(logo_path)
        logo = logo.resize((228, 50), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(logo)
        self.image_label = customtkinter.CTkLabel(self, image=self.photo, text="")
        self.image_label.grid(row=0, column=0, padx=(10, 0), pady=(10, 0), sticky="nw") """
        
        #def for each button
        #def for adding new deck
        def openDeck():
            print("launch studyMat GUI")
            
        def startGame():
            print("launch game GUI")
          
        #figure out frame   
        frame = customtkinter.CTkFrame(master=self, width=200, height=200)
        
        #icon for flashcards 
        flashcards = "flashcards3.png"
        cards = Image.open(flashcards)
        cards = cards.resize((426, 341), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(cards)
        self.img_label = customtkinter.CTkLabel(self, image=self.photo, text="")
        self.img_label.grid(row=9, column=8, padx=(10, 0), pady=(10, 0), sticky="nw")
        
        
        #button to edit deck
        editDeckButton = customtkinter.CTkButton(self, text="Create/Edit Deck", command=openDeck)
        editDeckButton.grid(row=12, column=7)
        #button to start new game
        startNewGame = customtkinter.CTkButton(self, text="Start New Game", command=startGame)
        startNewGame.grid(row=12, column=9)
        
        #reads data from json file - make method to process data and isolate it
        #will eventually make the structure so that each json file is a seperate deck of cards - and each thing is processed
        #Make icon with name of json file with buttons that reference the studyMat class to Review/Edit, and button to start game that 
        #creates instance of the game class
        
        #don't need to process contents of json file - just need to be able to display name - json file should be passed to studyMat class
        #to be able to open and process flashcards
        #start by creating  to this class
        
        #nvm we are going with just one flashcard deck for simplicity to get something up and working, so just add one icon in the middle and
        #configure the buttons to be beneath it
        """
        data = []
        with open('flashcards.json') as f:
            for line in f:
                data.append(json.loads(line))
            print(data)
        """
        
        """
        #open json
        def load_flashcards(self):
            try:
                with open("flashcards.json", "r") as file:
                    return json.load(file)
            except FileNotFoundError:
                return []
        """


customtkinter.set_default_color_theme("customTheme.json")
customtkinter.set_appearance_mode("dark")
app=home()
app.mainloop()

