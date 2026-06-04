from tkinter import *
window=Tk()

count=0
def click ():
    global count
    count+=1
    label.config(text=count)
    lbl.pack()


button=Button(window, text="Click me")
button.config(command=click) # calls the function and runs it
button.pack() # packing the button to use it in thr window
button.config(font=('Arial',50, 'bold'), bg='sky blue', fg='black')

img= PhotoImage(file="point.png")
button.config(image=img, compound=LEFT) # to add an image to the button and to specify the position of the image in the button

button.config(activebackground="black", activeforeground="sky blue") # attributes related to the color of button when it is active and when it is not

button.config(state=ACTIVE) # to disable the button and make it unclickable ACTIVE/DISABLED

label=Label(window, text=count)
label.config(font=('Monospace',50, 'bold'))
label.pack()


lbl=Label(window,image=img)
lbl.pack()
window.mainloop()