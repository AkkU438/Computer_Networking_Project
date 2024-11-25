from GUIConfig import GUIConfig
import customtkinter
import json


class FlashcardApp(GUIConfig):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("StudyBat Flashcards")
       
        self.current_card_index = 0
        self.flashcards = self.load_flashcards()
        self.showing_answer = False
       
        # Flashcard Number Label (Centered above question)
        self.card_number_label = customtkinter.CTkLabel(self, text="", justify="center")
        self.card_number_label.grid(row=1, column=0, columnspan=3, pady=(10, 5), sticky="ew")


        # Flashcard Question/Answer Label
        self.card_label = customtkinter.CTkLabel(self, text="", justify="center", wraplength=600)
        self.card_label.grid(row=2, column=0, columnspan=3, padx=20, pady=10, sticky="ew")


        # Buttons for flipping and navigation
        self.flip_button = customtkinter.CTkButton(self, text="Flip", command=self.flip_card)
        self.flip_button.grid(row=3, column=1, pady=10, padx = 10, sticky="ew")


        self.prev_button = customtkinter.CTkButton(self, text="Previous", command=self.prev_card)
        self.prev_button.grid(row=3, column=0, pady=10, padx = 10, sticky="ew")


        self.next_button = customtkinter.CTkButton(self, text="Next", command=self.next_card)
        self.next_button.grid(row=3, column=2, pady=10, padx = 10, sticky="ew")


        # Input fields for creating new flashcards
        self.new_question_entry = customtkinter.CTkEntry(self, placeholder_text="Enter question here")
        self.new_question_entry.grid(row=6, column=0, columnspan=3, padx=10, pady=5, sticky="ew")


        self.new_answer_entry = customtkinter.CTkEntry(self, placeholder_text="Enter answer here")
        self.new_answer_entry.grid(row=7, column=0, columnspan=3, padx=10, pady=5, sticky="ew")


        self.add_card_button = customtkinter.CTkButton(self, text="Add Flashcard", command=self.add_flashcard)
        self.add_card_button.grid(row=8, column=0, columnspan=3, padx=10, pady=10, sticky="ew")


        # Dropdown to select flashcard for editing or deletion
        self.selected_card_var = customtkinter.StringVar()
        self.card_dropdown = customtkinter.CTkComboBox(
            self, values=[], variable=self.selected_card_var, state="readonly"
        )
        self.card_dropdown.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky="ew")


        # Edit and Delete buttons
        self.edit_card_button = customtkinter.CTkButton(self, text="Edit", command=self.edit_flashcard)
        self.edit_card_button.grid(row=5, column=0, padx=10, pady=10, sticky="ew")


        self.delete_card_button = customtkinter.CTkButton(self, text="Delete", command=self.delete_flashcard)
        self.delete_card_button.grid(row=5, column=1, padx=10, pady=10, sticky="ew")


        self.save_button = customtkinter.CTkButton(self, text="Save", command=self.save_flashcards)
        self.save_button.grid(row=5, column=2, padx=10, pady=10, sticky="ew")


        # Display the first flashcard and populate dropdown
        self.display_card()
        self.update_dropdown()


    def load_flashcards(self):
        """ Load flashcards from a JSON file or return an empty list if the file doesn't exist. """
        try:
            with open("flashcards.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []


    def save_flashcards(self):
        """ Save the current flashcards to a JSON file. """
        with open("flashcards.json", "w") as file:
            json.dump(self.flashcards, file)
        self.update_dropdown()


    def update_dropdown(self):
        """ Update the dropdown menu with the current flashcards. """
        dropdown_values = [f"Flashcard {i + 1}: {card['question']}" for i, card in enumerate(self.flashcards)]
        self.card_dropdown.configure(values=dropdown_values)
        if self.flashcards:
            self.selected_card_var.set(dropdown_values[0])  # Default to the first flashcard


    def display_card(self):
        """ Display the current flashcard question or answer, along with its number. """
        if not self.flashcards:
            self.card_label.configure(text="No flashcards available. Add new flashcards below!")
            self.card_number_label.configure(text="")
            self.showing_answer = False
            return


        card = self.flashcards[self.current_card_index]
        card_number = f"Flashcard {self.current_card_index + 1} of {len(self.flashcards)}"
        self.card_number_label.configure(text=card_number)


        if self.showing_answer:
            self.card_label.configure(text=f"Answer:\n{card['answer']}")
        else:
            self.card_label.configure(text=f"Question:\n{card['question']}")


    def flip_card(self):
        """ Flip the flashcard to show the question or answer. """
        self.showing_answer = not self.showing_answer
        self.display_card()


    def next_card(self):
        """ Go to the next flashcard. """
        if not self.flashcards:
            return
        self.current_card_index = (self.current_card_index + 1) % len(self.flashcards)
        self.showing_answer = False
        self.display_card()


    def prev_card(self):
        """ Go to the previous flashcard. """
        if not self.flashcards:
            return
        self.current_card_index = (self.current_card_index - 1) % len(self.flashcards)
        self.showing_answer = False
        self.display_card()


    def add_flashcard(self):
        """ Add a new flashcard. """
        question = self.new_question_entry.get()
        answer = self.new_answer_entry.get()


        if question.strip() and answer.strip():
            self.flashcards.append({"question": question, "answer": answer})
            self.new_question_entry.delete(0, "end")
            self.new_answer_entry.delete(0, "end")
            self.update_dropdown()


    def delete_flashcard(self):
        """ Delete the selected flashcard. """
        if not self.flashcards:
            return


        selected_index = self.card_dropdown.cget("values").index(self.selected_card_var.get())
        self.flashcards.pop(selected_index)
        self.current_card_index = max(0, self.current_card_index - 1)
        self.update_dropdown()
        self.display_card()


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

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("customTheme.json")
app = FlashcardApp()
app.mainloop()