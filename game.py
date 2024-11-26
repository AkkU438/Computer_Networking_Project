
from studyMat import FlashcardApp
import customtkinter
import json
import random


class FlashcardGame(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Flashcard Game")
        self.geometry("800x600")
        self.points = 0
        self.current_flashcard = None
        self.flashcards = self.load_flashcards()
        random.shuffle(self.flashcards)

        # Display score
        self.score_label = customtkinter.CTkLabel(self, text=f"Score: {self.points}", font=("Arial", 20))
        self.score_label.pack(pady=20)

        # Flashcard question display
        self.question_label = customtkinter.CTkLabel(self, text="", font=("Arial", 20), wraplength=600, justify="center")
        self.question_label.pack(pady=20)

        # Answer entry
        self.answer_entry = customtkinter.CTkEntry(self, placeholder_text="Type your answer here", width=400)
        self.answer_entry.pack(pady=10)

        # Submit button
        self.submit_button = customtkinter.CTkButton(self, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

        # Load the first flashcard
        self.load_next_flashcard()

    def load_flashcards(self):
        """ Load flashcards from the JSON file. """
        try:
            with open("flashcards.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def load_next_flashcard(self):
        """ Load the next flashcard or end the game if there are no more cards. """
        if self.flashcards:
            self.current_flashcard = self.flashcards.pop()
            self.question_label.configure(text=f"Question: {self.current_flashcard['question']}")
            self.answer_entry.delete(0, "end")
        else:
            self.end_game()

    def check_answer(self):
        """ Check the user's answer and update the score. """
        user_answer = self.answer_entry.get().strip()
        correct_answer = self.current_flashcard["answer"]

        if user_answer.lower() == correct_answer.lower():
            self.points += 1
            self.score_label.configure(text=f"Score: {self.points}")
            self.question_label.configure(text="Correct! 🎉")
        else:
            self.question_label.configure(text=f"Incorrect! The correct answer was: {correct_answer}")

        self.after(2000, self.load_next_flashcard)  # Show next question after 2 seconds

    def end_game(self):
        """ End the game and display the final score. """
        self.question_label.configure(text=f"Game Over! Your final score is: {self.points}")
        self.answer_entry.destroy()
        self.submit_button.destroy()


if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("customTheme.json")
    app = FlashcardGame()
    app.mainloop()
