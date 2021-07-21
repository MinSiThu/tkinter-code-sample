from tkinter import *

window = Tk()
window.title("Welcome from tkinter")

#lb1 = Label(window,text="This is a label",font=("Arial Bold",50))
lb1 = Label(window,text="This is a label")
lb1.grid(row=0,column=0)

txtInput = Entry(window,width=10)
txtInput.grid(row=0,column=1)

def onClicked():
    text = txtInput.get()
    lb1.configure(text=text)

btn = Button(window,text="This is a button",bg="orange",fg="red",command=onClicked)
btn.grid(row=0,column=2)

window.geometry("650x450")
window.mainloop()