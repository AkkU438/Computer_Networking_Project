import customtkinter
from PIL import Image, ImageTk

        

class loginGUI(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #Standardized window size + grid: 28 columns (0-27) and 20 rows (0-19)
        self.title("loginGUI")
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
        
        #sign up information 
        #store username and password in dictionary, use initial ones for testing
        securityCheck = {"username": "password123"}
        
        #currently, have to sign up each session to be able to log in
        def signUp():
            if(passEntry.get() == ""):
                print("enter pass")
            if(userEntry.get() == ""):
                print("enter user")
            
            #takes data in from entry fields and adds to dictionary
            securityCheck[userEntry.get()] = passEntry.get()
            #clears entry boxes
            userEntry.delete(0, customtkinter.END)
            passEntry.delete(0, customtkinter.END)
            print(securityCheck)#checking variable, delete later
            #then go to main page(?), add code later
            
        def log_in():
            if(passEntry.get() == ""):
                errorMessage = customtkinter.CTkLabel(self, text="Please enter a password", fg_color="transparent", text_color="gray14", font=("Agency FB Bold", 20))
                errorMessage.grid(row=13, column=8, sticky='ew')
            if(userEntry.get() == ""):
                errorMessage = customtkinter.CTkLabel(self, text="Please enter a username", fg_color="transparent", text_color="gray14", font=("Agency FB Bold", 20))
                errorMessage.grid(row=13, column=8, sticky='ew')
            
            user = False
            enteredUser = userEntry.get()
            enteredPass = passEntry.get()
            
            for username, password in securityCheck.items():
                if((username == enteredUser) & (password == enteredPass)):
                    user = True
                     
            if((passEntry.get() != "")&(userEntry.get() != "")&(user == True)):
                errorMessage = customtkinter.CTkLabel(self, text="Login successful!", fg_color="transparent", text_color="gray14", font=("Agency FB Bold", 20))
                errorMessage.grid(row=13, column=8, sticky='ew')
                userEntry.delete(0, customtkinter.END)
                passEntry.delete(0, customtkinter.END)
                #go to home
                
            elif((passEntry.get() != "")&(userEntry.get() != "")):
                errorMessage = customtkinter.CTkLabel(self, text="User not found, please sign up or try again.", fg_color="transparent", text_color="gray14", font=("Agency FB Bold", 20))
                errorMessage.grid(row=13, column=8, sticky='ew')

        #GUI elements
        #button
        signUpButton = customtkinter.CTkButton(self, text="Sign Up", command=signUp)
        signUpButton.grid(row=12, column=7)
        loginButton = customtkinter.CTkButton(self, text="Login", command=log_in)
        loginButton.grid(row=12, column=9)
        #password/username entry
        userEntry = customtkinter.CTkEntry(self, placeholder_text="Username")
        userEntry.grid(row=10, column=7, columnspan=3, sticky='ew')
        passEntry = customtkinter.CTkEntry(self, placeholder_text="Password")
        passEntry.grid(row=11, column=7, columnspan=3, sticky='ew')
        #labels
        loginLabel = customtkinter.CTkLabel(self, text="Login/Sign Up", fg_color="transparent", text_color="gray14", font=("Agency FB Bold", 40))
        loginLabel.grid(row=9, column=8, sticky='ew')


#main app window/start page:
class main(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
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
        
        #start button + label
        self.label = customtkinter.CTkLabel(self, text="Welcome to StudyBat!", font=("Agency FB Bold", 40))
        self.label.grid(row=10, column=9, sticky="ew")
        self.button = customtkinter.CTkButton(self, command=self.button_click, text="Start")
        self.button.grid(row=12, column=9, sticky="ew")

        self.toplevel_window = None
    
    
    # add methods to app
    def button_click(self):#opens login
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = loginGUI()  # create window if its None or destroyed
        self.toplevel_window.focus() #TODO: fix focus
        


customtkinter.set_default_color_theme("customTheme.json")
customtkinter.set_appearance_mode("dark")
app = main()
app.mainloop()
