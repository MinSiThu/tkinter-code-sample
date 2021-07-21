from tkinter import *

window = Tk()
window.title("File Dialog Tkinter")
window.geometry("450x450")

menu = Menu(window)

def onClicked():
    print("New Item was clicked")

menu_item = Menu(menu,tearoff=0)
menu_item.add_command(label='New',command=onClicked)
menu_item.add_separator()
menu_item.add_command(label="Edit")

menu.add_cascade(label='File', menu=menu_item)

window.config(menu=menu)
window.mainloop()