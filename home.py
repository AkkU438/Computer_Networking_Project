from PIL import Image, ImageTk
import customtkinter
from SceneManager import SceneManager

class home(SceneManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #Standardized window size + grid: 28 columns (0-27) and 20 rows (0-19)
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
        self.image_label.grid(row=0, column=0, padx=(10, 0), pady=(10, 0), sticky="nw")
        
        #icon for flashcards 
        flashcards = "flashcards3.png"
        cards = Image.open(flashcards)
        cards = cards.resize((426, 341), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(cards)
        self.img_label = customtkinter.CTkLabel(self, image=self.photo, text="")
        self.img_label.grid(row=9, column=7, padx=(10, 0), pady=(10, 0), sticky="nw")
        
        
        #button to edit deck
        editDeckButton = customtkinter.CTkButton(self, text="Create/Edit Deck", command=lambda: SceneManager.show_scene("Home"))
        editDeckButton.grid(row=12, column=6)
        #button to start new game
        startNewGame = customtkinter.CTkButton(self, text="Start New Game", command=lambda: SceneManager.show_scene("Home"))
        startNewGame.grid(row=12, column=8)

customtkinter.set_default_color_theme("customTheme.json")
customtkinter.set_appearance_mode("dark")
app=home()
app.mainloop()
