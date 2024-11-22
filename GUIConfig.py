from PIL import Image, ImageTk
import customtkinter

class GUIConfig(customtkinter.CTk):
    def __init__(self, master=None, **kwargs):
        super().__init__()

        #Standardized window size + grid: 28 columns (0-27) and 20 rows (0-19)
        self.title("studyBat")
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
        
        
