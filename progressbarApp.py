from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk

window = Tk()
window.title("Progress bar App tkinter")
window.geometry("450x450")

style = ttk.Style()
style.theme_use("default")

progressbar = Progressbar(window,length=220,orient = HORIZONTAL,mode = 'indeterminate')
progressbar.value = 10

progressbar.grid(row=0,column=0)

window.mainloop()