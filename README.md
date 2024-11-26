# Computer_Networking_Project
This is our Computer Networking Project for CSI 2470
Group Members: Michael Medulla, Hannah Fosnaugh, Aditya Kurup

We plan to create a program that allows the user to create a trivia deck that they can use to study with stuff they already learned. We used UDP to communicate between a server.py file and our game. The UDP communication just allowed us to keep track of the players score. 

How to Run:
Step 0: First make sure that you have python and pip installed (latest version). Then use “pip install pillow” and “pip install customtkinter”

Step 1: Open two command prompts, in the first command prompt run the server file (python server.py), and in the other command prompt run the main file (python main.py)

Step 2: Create login credentials so that you can use the application. You just have to create a new username and password then click register. Afterwards sign in using your new credentials.

Step 3: Create new flashcards. Fill out the “Question” and “Answer” fields in the flashcard page, and then click “Add” to create a flashcard with these attributes. To edit/delete pre-existing flashcards just use the scroll down menu and click “Delete” to delete them, or fill out a new question and answer field and click the “Edit” button to change the flashcard attributes. You can additionally, use the “Flip”, “Previous” , and “Next” buttons to cycle through the flashcards and flip to see the answer to the flashcards. Finally, you can click the “Save” button to save the flashcards you created. 

Step 4: Then you can click the “New Game” button to play the flash card game. The flashcards you created are shuffled and you get a point for each question you get right.

Step 5: After you are done, you can exit the game or create another set of cards to play the game again. 
