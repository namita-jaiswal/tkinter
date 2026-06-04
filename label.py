# label = an area widget that holds text and/or an image within an window
from tkinter import *
window = Tk()

photo=PhotoImage(file='penguin.png')

label=Label(window,
            text="neggawatt",
            font=("Calibri", 40, "bold"),
            fg="#a71a5c", bg="#5078B3",
            relief=RAISED, bd=10,
            padx=20, pady=20,
            image=photo,
            compound='bottom')
# padding (padx and pady) adds space around the text in the label fromt he borders in pixels


label.pack() # used to display labels on the window
# label.place() # used to place the label at a specific location on the window through coordinates
 
window.mainloop()