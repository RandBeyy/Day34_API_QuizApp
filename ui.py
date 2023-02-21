import tkinter as tk

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = tk.Tk()
        self.config_window()

        self.score = tk.Label(self.window, background=THEME_COLOR, text="Score: 0", font="Arial 10")

        self.canvas = tk.Canvas(self.window, width=300, height=250, bg="gray")

        false_image = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(self.window, image=false_image, command=lambda: print("hi"))
        
        true_image = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(self.window, image=true_image, command=lambda: print("hi"))

        self.place_widgets()
        self.window.mainloop()


    def config_window(self):
        self.window.title("Quizzler")
        self.window.geometry("340x500")
        self.window.configure(bg=THEME_COLOR)
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.rowconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=4)
        self.window.rowconfigure(2, weight=1)

    def place_widgets(self):
        self.score.grid(row=0, column=1, sticky=tk.EW)
        self.canvas.grid(row=1, sticky=tk.EW, columnspan=2, padx=20)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

if __name__ == "__main__":
    quiz = QuizInterface()
