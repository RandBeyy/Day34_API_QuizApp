import tkinter as tk
from quiz_brain import QuizBrain
from tkinter import messagebox

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.window = tk.Tk()
        self._config_window()
        self.quiz = quiz

        self.score = tk.Label(self.window, background=THEME_COLOR, text="Score: 0", font="Arial 10")

        self.canvas = tk.Canvas(self.window, width=300, height=250, bg="gray")
        self.word = self.canvas.create_text((150, 125), text="Русня йобана", font="Arial 10 bold")

        false_image = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(self.window, image=false_image, command=lambda: self._check_answer(False))
        
        true_image = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(self.window, image=true_image, command=lambda: self._check_answer(True))

        self._place_widgets()

        self._show_next_question()
        self.window.mainloop()


    def _config_window(self):
        self.window.title("Quizzler")
        self.window.geometry("340x500")
        self.window.configure(bg=THEME_COLOR)
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.rowconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=4)
        self.window.rowconfigure(2, weight=1)


    def _place_widgets(self):
        self.score.grid(row=0, column=1, sticky=tk.EW)
        self.canvas.grid(row=1, sticky=tk.EW, columnspan=2, padx=20)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

    def _check_for_line_break(self, text):
        amount_of_line_breaks = len(text) // 36
        for i in range(amount_of_line_breaks):
            character_position = (i + 1) * 36
            text = text[:character_position] + "\n" + text[character_position:]
        return text


    def _show_next_question(self):
        if self.quiz.still_has_questions():
            question_text = self._check_for_line_break(self.quiz.next_question())
            self.canvas.itemconfig(self.word, text=question_text)
        else: messagebox.showinfo(title="Quiz is over", message=f"Your score is {self.quiz.score}")
    
    def _check_answer(self, answer: bool):
        self._show_next_question()
        if self.quiz.check_answer(answer):
            self.score.configure(text=f"Score: {self.quiz.score}")



if __name__ == "__main__":
    quiz = QuizInterface()
