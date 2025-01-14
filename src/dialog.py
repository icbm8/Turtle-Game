import tkinter as tk
from tkinter import simpledialog

class QuestionDialog:
    def __init__(self):
        # Initialize the root window but keep it hidden
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the root window

    def show_dialog(self, question, correct_answer):
        # Show the input dialog with the question
        user_input = simpledialog.askstring("Input", question)

        # Check if the user input matches the correct answer (case-sensitive check)
        if user_input == correct_answer:
            return True
        else:
            return False

    def close(self):
        # Close the tkinter root window when done
        self.root.quit()


