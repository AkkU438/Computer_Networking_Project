from PIL import Image, ImageTk
import customtkinter

class GUIConfig(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        #Standardized window size + grid: 28 columns (0-27) and 20 rows (0-19)
        self.title("studyBat")
        self.geometry("1050x750") #window size
        self.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27), weight=1)
        self.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19), weight=1)

        #Example for how to add widgets/elements with grid, look at documentation for more information: https://customtkinter.tomschimansky.com
        """ self.button1 = customtkinter.CTkButton(self, text="Login")
        self.button1.grid(row=1, column=0, sticky="nw")
        
        self.button2 = customtkinter.CTkButton(self, text="Login")
        self.button2.grid(row=1, column=1, sticky="nw")
        
        self.button3 = customtkinter.CTkButton(self, text="Login")
        self.button3.grid(row=15, column=27, sticky="w") """
        
           
        #Adds logo to top left corner
        logo_path = "StudyBat_Logo.png"
        logo = Image.open(logo_path)
        logo = logo.resize((228, 50), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(logo)
        self.image_label = customtkinter.CTkLabel(self, image=self.photo, text="")
        self.image_label.grid(row=0, column=0, padx=(10, 0), pady=(10, 0), sticky="nw")
        
        
    

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("customTheme.json")
app = GUIConfig()
app.mainloop()

