from PIL import Image, ImageTk
import customtkinter
from GUIConfig import GUIConfig

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
        def createNewDeck():
            print("launch new deck GUI")
        
        
        #button to add new deck
        addDeckButton = customtkinter.CTkButton(self, text="Add Deck", command=createNewDeck)
        addDeckButton.grid(row=0, column=26)
        
        
        startNewGame = customtkinter.CTkButton(self, text="Start New Game")
        startNewGame.grid(row=1, column=26)


customtkinter.set_default_color_theme("customTheme.json")
customtkinter.set_appearance_mode("dark")
app=home()
app.mainloop()

