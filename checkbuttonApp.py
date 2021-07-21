from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("From Tkinter tuts 3")
window.geometry("300x500")

checkState = BooleanVar()
checkState.set(True)

checkBox = Checkbutton(window,text="Check it",var=checkState)
checkBox.grid(row=0,column=0)

window.mainloop()