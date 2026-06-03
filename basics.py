from tkinter import *
window=Tk()

window.geometry("420x420") #changing the size of the window

window.title("Nam") #changing the title of the window

icon=PhotoImage(file="image.png") #gotta convert png to PhotoImage format
window.iconphoto(True,icon)

window.config(background="sky blue") #changing the background color of the window

window.mainloop() #adds a blank window