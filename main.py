import customtkinter
from PIL import Image, ImageTk
import json
import random
import socket




class game(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #Standardized window size + grid: 28 columns (0-27) and 20 rows (0-19)
        self.title("Game")
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
        
        self.points = 0
        self.server_points = 0
        self.current_flashcard = None
        self.flashcards = self.load_flashcards()
        random.shuffle(self.flashcards)
        #Home top level
        self.topLevelHome = None        

        #Display score
        self.score_label = customtkinter.CTkLabel(self, text=f"Score: {self.points}")
        self.score_label.grid(row=1, column=2, sticky="ew")

        #Flashcard question
        self.question_label = customtkinter.CTkLabel(self, text="", wraplength=600, justify="center")
        self.question_label.grid(row=2, column=2, sticky="ew")

        #Answer entry
        self.answer_entry = customtkinter.CTkEntry(self, placeholder_text="Type your answer here", width=400)
        self.answer_entry.grid(row=3, column=2, sticky="ew")

        #Submit button
        self.submit_button = customtkinter.CTkButton(self, text="Submit", command=self.check_answer)
        self.submit_button.grid(row=4, column=2, sticky="ew")

        #Load first flashcard
        self.load_next_flashcard()

    #Load flashcards from JSON
    def load_flashcards(self):
        try:
            with open("flashcards.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    #Load next flashcard/end game
    def load_next_flashcard(self):
        if self.flashcards:
            self.current_flashcard = self.flashcards.pop()
            self.question_label.configure(text=f"Question: {self.current_flashcard['question']}")
            self.answer_entry.delete(0, "end")
        else:
            self.end_game()


    #Check user answer/update score
    def check_answer(self):
        user_answer = self.answer_entry.get().strip()
        
        #Connects with server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("127.0.0.1", 65432))
        
        correct_answer = self.current_flashcard["answer"]

        if user_answer.lower() == correct_answer.lower():
            self.points += 1
            self.score_label.configure(text=f"Score: {self.points}")
            self.question_label.configure(text="Correct!")
            server_message = f"That's right!\nServer: {self.server_points}\nYou: {self.points}"
            client_socket.sendall(server_message.encode())
        else:
            self.server_points+=1
            self.question_label.configure(text=f"Incorrect. The correct answer was: {correct_answer}")
            server_message = f"That's wrong, one point for me!\nServer: {self.server_points}\nYou: {self.points}"
            client_socket.sendall(server_message.encode())

        self.after(1000, self.load_next_flashcard)  #Show next question after 1 second

    def quitToHome(self):
        if self.topLevelHome is None or not self.topLevelHome.winfo_exists():
                self.topLevelHome = home()
        self.topLevelHome.focus()

    #Display final score
    def end_game(self):
        #Connects with server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("127.0.0.1", 65432))
        
        self.question_label.configure(text=f"Game over.\nYour final score is {self.points}")
        
        server_message = "Game over"
        if(self.server_points>self.points):
            server_message = "Server wins! Better luck next time."
        if(self.server_points<self.points):
            server_message = "You won! Nice job :)"
        if(self.server_points==self.points):
            server_message = "It's a tie! Better try again..."
        
        client_socket.sendall(server_message.encode())
        self.answer_entry.destroy()
        self.submit_button.destroy()
        #Quit to home button
        self.quitHome = customtkinter.CTkButton(self, text="Quit to Home", command=self.quitToHome)
        self.quitHome.grid(row=6, column=2, sticky="ew")
 #problem - missing socket programming - add


#Edit/Create Flashcards Class
class studyMat(customtkinter.CTkToplevel):#changed file name
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #Standardized window size + grid: 28 columns (0-27) and 20 rows (0-19)
        self.title("Create/Edit Deck")
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
        #top level windows
        self.topLevelGame = None
        self.topLevelReturnToHome = None
        
        #Other initializations
        self.current_card_index = 0
        self.flashcards = self.load_flashcards()
        self.showing_answer = False
       
        # Flashcard Number Label (Centered above question)
        self.card_number_label = customtkinter.CTkLabel(self, text="", justify="center")
        self.card_number_label.grid(row=1, column=1, columnspan=3, pady=(10, 5), sticky="ew")


        # Flashcard Question/Answer Label
        self.card_label = customtkinter.CTkLabel(self, text="", justify="center", wraplength=600)
        self.card_label.grid(row=2, column=1, columnspan=3, padx=20, pady=10, sticky="ew")


        # Buttons for flipping and navigation
        # Button for flipping flashcards to show answer
        self.flip_button = customtkinter.CTkButton(self, text="Flip", command=self.flip_card)
        self.flip_button.grid(row=3, column=2, pady=10, padx = 10, sticky="ew")

        # Button for going to the previous flashcard
        self.prev_button = customtkinter.CTkButton(self, text="Previous", command=self.prev_card)
        self.prev_button.grid(row=3, column=1, pady=10, padx = 10, sticky="ew")

        # Button for going to the next available flashcard
        self.next_button = customtkinter.CTkButton(self, text="Next", command=self.next_card)
        self.next_button.grid(row=3, column=3, pady=10, padx = 10, sticky="ew")


        # Input fields for creating new flashcards
        # Field for questions
        # Writing new questions for the flashcards
        self.new_question_entry = customtkinter.CTkEntry(self, placeholder_text="Enter question here")
        self.new_question_entry.grid(row=6, column=1, columnspan=3, padx=10, pady=5, sticky="ew")

        # Field for answers
        self.new_answer_entry = customtkinter.CTkEntry(self, placeholder_text="Enter answer here")
        self.new_answer_entry.grid(row=7, column=1, columnspan=3, padx=10, pady=5, sticky="ew")

        # Adds Flashcards
        self.add_card_button = customtkinter.CTkButton(self, text="Add Flashcard", command=self.add_flashcard)
        self.add_card_button.grid(row=8, column=1, columnspan=3, padx=10, pady=10, sticky="ew")


        # Dropdown to select flashcard for editing or deletion
        self.selected_card_var = customtkinter.StringVar()
        self.card_dropdown = customtkinter.CTkComboBox(
            self, values=[], variable=self.selected_card_var, state="readonly"
        )
        self.card_dropdown.grid(row=4, column=1, columnspan=3, padx=10, pady=10, sticky="ew")


        # Edit and Delete buttons
        # Edits exisiting flashcards
        self.edit_card_button = customtkinter.CTkButton(self, text="Edit", command=self.edit_flashcard)
        self.edit_card_button.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

        # Deletes exisiting flashcards
        self.delete_card_button = customtkinter.CTkButton(self, text="Delete", command=self.delete_flashcard)
        self.delete_card_button.grid(row=5, column=2, padx=10, pady=10, sticky="ew")

        # Saves existing flashcards
        self.save_button = customtkinter.CTkButton(self, text="Save", command=self.save_flashcards)
        self.save_button.grid(row=5, column=3, padx=10, pady=10, sticky="ew")
        
        #Buttons for entering game or returning to home
        self.newGame = customtkinter.CTkButton(self, text="Start New Game", command=self.startNewGame)
        self.newGame.grid(row=9, column=1, padx=10)
        
        self.returnToHome = customtkinter.CTkButton(self, text="Return To Home", command=self.returnHome)
        self.returnToHome.grid(row=9, column=2, padx=10)


        # Display the first flashcard and populate dropdown
        self.display_card()
        self.update_dropdown()

        # Opens the JSON file
    def load_flashcards(self):
        """ Load flashcards from a JSON file or return an empty list if the file doesn't exist. """
        try:
            with open("flashcards.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

        # Loads the flashcards the JSON file
    def save_flashcards(self):
        """ Save the current flashcards to a JSON file. """
        with open("flashcards.json", "w") as file:
            json.dump(self.flashcards, file)
        self.update_dropdown()

        # Updates the dropdown so that the user can delete and edit for 
    def update_dropdown(self):
        """ Update the dropdown menu with the current flashcards. """
        dropdown_values = [f"Flashcard {i + 1}: {card['question']}" for i, card in enumerate(self.flashcards)]
        self.card_dropdown.configure(values=dropdown_values)
        if self.flashcards:
            self.selected_card_var.set(dropdown_values[0])  # Default to the first flashcard

        # Displays for flashcards and their number
    def display_card(self):
        """ Display the current flashcard question or answer, along with its number. """
        if not self.flashcards:
            self.card_label.configure(text="No flashcards available. Add new flashcards below!")
            self.card_number_label.configure(text="")
            self.showing_answer = False
            return

        # Counter for flashcard number
        card = self.flashcards[self.current_card_index]
        card_number = f"Flashcard {self.current_card_index + 1} of {len(self.flashcards)}"
        self.card_number_label.configure(text=card_number)

        # Shows answers
        if self.showing_answer:
            self.card_label.configure(text=f"Answer:\n{card['answer']}")
        else:
            self.card_label.configure(text=f"Question:\n{card['question']}")

        # Flip cards to show answer or question
    def flip_card(self):
        """ Flip the flashcard to show the question or answer. """
        self.showing_answer = not self.showing_answer
        self.display_card()

        # Goes to the next card
    def next_card(self):
        """ Go to the next flashcard. """
        if not self.flashcards:
            return
        self.current_card_index = (self.current_card_index + 1) % len(self.flashcards)
        self.showing_answer = False
        self.display_card()

        # Go to the previous card
    def prev_card(self):
        """ Go to the previous flashcard. """
        if not self.flashcards:
            return
        self.current_card_index = (self.current_card_index - 1) % len(self.flashcards)
        self.showing_answer = False
        self.display_card()

        # Go adds a new flashcard
    def add_flashcard(self):
        """ Add a new flashcard. """
        question = self.new_question_entry.get()
        answer = self.new_answer_entry.get()

        # Adds a new flashcard to deck
        if question.strip() and answer.strip():
            self.flashcards.append({"question": question, "answer": answer})
            self.new_question_entry.delete(0, "end")
            self.new_answer_entry.delete(0, "end")
            self.update_dropdown()

        # Deletes a flashcard from the deck
    def delete_flashcard(self):
        """ Delete the selected flashcard. """
        if not self.flashcards:
            return

                
        selected_index = self.card_dropdown.cget("values").index(self.selected_card_var.get())
        self.flashcards.pop(selected_index)
        self.current_card_index = max(0, self.current_card_index - 1)
        self.update_dropdown()
        self.display_card()

        # Edits this flashcard
    def edit_flashcard(self):
        """ Edit the selected flashcard. """
        if not self.flashcards:
            return


        selected_index = self.card_dropdown.cget("values").index(self.selected_card_var.get())
        question = self.new_question_entry.get()
        answer = self.new_answer_entry.get()


        if question.strip():
            self.flashcards[selected_index]["question"] = question
        if answer.strip():
            self.flashcards[selected_index]["answer"] = answer


        self.new_question_entry.delete(0, "end")
        self.new_answer_entry.delete(0, "end")
        self.update_dropdown()
        self.display_card() 
        
    #Switching page button defs
    def startNewGame(self):
        if self.topLevelGame is None or not self.topLevelGame.winfo_exists():
            self.topLevelGame = game()  #add game file
        self.topLevelGame.focus() #TODO: fix focus
        
    def returnHome(self):
        if self.topLevelReturnToHome is None or not self.topLevelReturnToHome.winfo_exists():
            self.topLevelReturnToHome = home() 
        self.topLevelReturnToHome.focus() #TODO: fix focus      
        
    


#Main Home Class
class home(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #Standardized window size + grid: 28 columns (0-27) and 20 rows (0-19)
        self.title("Home")
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
        #top level windows
        self.topLevelGame = None
        self.topLevelStudyMat = None
        
        #def for each button
        #def for adding new deck
        def openDeck():
            if self.topLevelStudyMat is None or not self.topLevelStudyMat.winfo_exists():
                self.topLevelStudyMat = studyMat()  #add studyMat file
            self.topLevelStudyMat.focus() #TODO: fix focus
            
        def startGame():
            if self.topLevelGame is None or not self.topLevelGame.winfo_exists():
                self.topLevelGame = game()  #add game file
            self.topLevelGame.focus() #TODO: fix focus
        
        #GUI Elements
        #Icon for flashcards 
        flashcards = "flashcards3.png"
        cards = Image.open(flashcards)
        cards = cards.resize((426, 341), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(cards)
        self.img_label = customtkinter.CTkLabel(self, image=self.photo, text="")
        self.img_label.grid(row=9, column=7, padx=(10, 0), pady=(10, 0), sticky="nw")
        
        #button to edit deck
        editDeckButton = customtkinter.CTkButton(self, text="Create/Edit Deck", command=openDeck)
        editDeckButton.grid(row=12, column=6)
        #button to start new game
        startNewGame = customtkinter.CTkButton(self, text="Start New Game", command=startGame)
        startNewGame.grid(row=12, column=8)


  
#LoginGUI Class
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
        #maybe toy with - button config
        self.toplevel_window = None     
        
        #sign up information 
        #store username and password in dictionary, use initial ones for testing
        securityCheck = {"u": "p"}
        
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
            
        def goToHome(self):#opens login
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = home()  # create window if its None or destroyed
            self.toplevel_window.focus() #TODO: fix focus    
            
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
                goToHome(self)#works! just still focus issue          
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
    def __init__(self):
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
    
    def button_click(self):#opens login
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = loginGUI()  # create window if its None or destroyed
        self.toplevel_window.focus() #TODO: fix focus
        
    
        


customtkinter.set_default_color_theme("customTheme.json")
customtkinter.set_appearance_mode("dark")
app = main()
app.mainloop()
