from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Tab View App Tkinter")
window.geometry("500x500")

tabController = ttk.Notebook(window)
tab1 = ttk.Frame(tabController)
tab2 = ttk.Frame(tabController)

tabController.add(tab1,text="Tab 1")
tabController.add(tab2,text="Tab 2")

lb1 = Label(tab1,text="Label1")
lb2 = Label(tab2,text='Label2')

lb1.grid(row=0,column=0)
lb2.grid(row=0,column=0)

tabController.pack(expand=1,fill="both")

window.mainloop()