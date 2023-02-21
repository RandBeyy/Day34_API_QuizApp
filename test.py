import tkinter as tk

window = tk.Tk()
window.title("Quizzler")
window.geometry("340x500")
true_image = tk.PhotoImage(file="images/true.png")
true_button = tk.Button(window, image=true_image, command=lambda: print("hi"))
true_button.grid(row=2, column=0)

window.mainloop()
