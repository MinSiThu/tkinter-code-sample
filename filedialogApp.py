from tkinter import *
from tkinter import filedialog

window = Tk()
window.title("File Dialog Tkinter App")
window.geometry("450x450")

def onClicked():
    file = filedialog.askopenfilename()
    print(file)

button = Button(window,text="Open File Explorer",command=onClicked)
button.grid(row=0,column=0)

window.mainloop()