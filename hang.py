from tkinter import * # imports all the classes, functions from tkinter lib

word = "python" # secret word
guessed = "" # stores the correct guessed words in this empty variable
lives = 6 # no. of lives 6




def draw_hangman():
    stage = 6 - lives # stage decides which part to draw (arm, leg, head)

    if stage == 1:
        canvas.create_oval(130, 50, 170, 90, width=2)  # Draws the head (oval)

    elif stage == 2:
        canvas.create_line(150, 90, 150, 150, width=2)  # Body (vertical line)

    elif stage == 3:
        canvas.create_line(150, 110, 120, 130, width=2)  # Left Arm (slant line)

    elif stage == 4:
        canvas.create_line(150, 110, 180, 130, width=2)  # Right Arm (slant line)

    elif stage == 5:
        canvas.create_line(150, 150, 120, 190, width=2)  # Left Leg (slant line)

    elif stage == 6:
        canvas.create_line(150, 150, 180, 190, width=2)  # Right Leg (slant line)




def check():
    global guessed, lives

    letter = entry.get().lower() # displays in lowercase
    entry.delete(0, END) # clears the enrty widget for next input

    if letter in word:
        guessed += letter # if letter entered by the user is correct then it is stored in the empty variable 'guessed' (line 4)
    else:
        lives -= 1 # if letter isnt correct then lives reduce by 1
        draw_hangman() # called

    display = "" # creates an empty string of guessed word

    for ch in word:
        if ch in guessed:
            display += ch + " " # if guessed word is correct the character is displayed, othw else condition displays an underscore
        else:
            display += "_ "




# label = an area widget that holds text and/or an image within an window
    word_label.config(text=display) # word label (_ _ _ _ _ _)
    lives_label.config(text="Lives: " + str(lives)) # live label

    if "_" not in display:
        result_label.config(text="You Win!") # if underscores are not in display that means letter have been guessed then display a winning msg

    elif lives == 0:
        result_label.config(text="You Lose! Word: " + word) # if underscores are in display and lives are zero that means user lost




root = Tk() # displays window
root.title("Hangman") # title of the window
root.geometry("350x500") # dimensions of the window

# canvas for hangman
canvas = Canvas(root, width=250, height=220, bg="#b44f35")
canvas.pack(pady=10)

canvas.create_line(50, 200, 200, 200, width=2) # base
canvas.create_line(80, 200, 80, 30, width=2) # pole
canvas.create_line(80, 30, 150, 30, width=2) # top beam
canvas.create_line(150, 30, 150, 50, width=2) # rope




word_label = Label(root, text="_ _ _ _ _ _", font=("Arial", 20))
word_label.pack(pady=10) # packing the word label to display on the window

entry = Entry(root)
entry.pack() # packing the entry widget to display on the window

Button(root, text="Guess", command=check).pack(pady=10)

lives_label = Label(root, text="Lives: 6")
lives_label.pack() # packing the button widget to display on the window

result_label = Label(root, font=("Arial", 12))
result_label.pack(pady=10) # shows your activity, if the user won or lost

root.mainloop() # runs the code in loop and handles all function calls