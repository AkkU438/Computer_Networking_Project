from PIL import Image, ImageTk
import customtkinter
from GUIConfig import GUIConfig
from home import home

class loginGUI(GUIConfig):
    def __init__(self, parent=None):
        super().__init__(parent)
        
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
        
