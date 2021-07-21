from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Message Box Appp Tkinter")
window.geometry("450x450")

def onClicked1():
    messagebox.showinfo("Info Box Message","Message Content")

def onClicked2():
    messagebox.showwarning("Info Warning Message","Message Content")

def onClicked3():
    messagebox.showerror("Info Error Message","Message Content")

def onClicked4():
    result = messagebox.askquestion("this is question dialog","Content")
    print(result)

btn1 = Button(window,text="Show Message Box",command=onClicked1)
btn1.grid(row=0,column=0)

btn2 = Button(window,text="Show Warning Box",command=onClicked2)
btn2.grid(row=0,column=1)

btn3 = Button(window,text="Show Alert Box",command=onClicked3)
btn3.grid(row=0,column=2)

btn4 = Button(window,text="Ask Question Dialog",command=onClicked4)
btn4.grid(row=1,column=0)

window.mainloop()