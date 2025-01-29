from tkinter import *
import webbrowser


def fun1():
    webbrowser.open("https://www.youtube.com/watch?v=21FnnGKSRZo&t=139s")


root = Tk()
root.title("PYTHONNNNN LAAAAB")
root.geometry("400x900")
button = Button(root, text="click me", fg="blue", bg="yellow", font="helvatica 20 bold", padx=50, pady=50, command=fun1)
# widget
button.pack(side=LEFT)

root.mainloop()


