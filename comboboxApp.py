from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
window.title("This is from tkinter 2")
window.geometry("300x300")

combobox1 = Combobox(window)
combobox1["values"] = (1,2,3,4,5,"Text")
combobox1.grid(row=0,column=0)
combobox1.current(3)

window.mainloop()