from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title('Radio Button Tkinter')
window.geometry("450x450")

def onClicked():
    print(selectedValue.get())

selectedValue = IntVar()

radioBtn1 = Radiobutton(window,text="One",value=1,variable=selectedValue)
radioBtn2 = Radiobutton(window,text="Two",value=2,variable=selectedValue)
radioBtn3 = Radiobutton(window,text="Three",value=3,variable=selectedValue)

radioBtn1.grid(row=0,column=0)
radioBtn2.grid(row=0,column=1)
radioBtn3.grid(row=0,column=2)

btn = Button(window,text='Choose',command=onClicked)
btn.grid(row=0,column=4)

window.mainloop()
