from tkinter import *
from tkinter import scrolledtext

window = Tk()
window.title("Scrolled Text App")
window.geometry("450x450")

textArea = scrolledtext.ScrolledText(window)
textArea.grid(row=0,column=0)

window.mainloop()