from tkinter import *

word = "python"
guessed = ""
lives = 6

def draw_hangman():
    stage = 6 - lives

    if stage == 1:
        canvas.create_oval(130, 50, 170, 90, width=2)  # Head

    elif stage == 2:
        canvas.create_line(150, 90, 150, 150, width=2)  # Body

    elif stage == 3:
        canvas.create_line(150, 110, 120, 130, width=2)  # Left Arm

    elif stage == 4:
        canvas.create_line(150, 110, 180, 130, width=2)  # Right Arm

    elif stage == 5:
        canvas.create_line(150, 150, 120, 190, width=2)  # Left Leg

    elif stage == 6:
        canvas.create_line(150, 150, 180, 190, width=2)  # Right Leg


def check():
    global guessed, lives

    letter = entry.get().lower()
    entry.delete(0, END)

    if letter in word:
        guessed += letter
    else:
        lives -= 1
        draw_hangman()

    display = ""

    for ch in word:
        if ch in guessed:
            display += ch + " "
        else:
            display += "_ "

    word_label.config(text=display)
    lives_label.config(text="Lives: " + str(lives))

    if "_" not in display:
        result_label.config(text="You Win!")

    elif lives == 0:
        result_label.config(text="You Lose! Word: " + word)


root = Tk()
root.title("Hangman")
root.geometry("350x500")

# Canvas for hangman
canvas = Canvas(root, width=250, height=220, bg="#b44f35")
canvas.pack(pady=10)

# Gallows
canvas.create_line(50, 200, 200, 200, width=2)
canvas.create_line(80, 200, 80, 30, width=2)
canvas.create_line(80, 30, 150, 30, width=2)
canvas.create_line(150, 30, 150, 50, width=2)

word_label = Label(root, text="_ _ _ _ _ _", font=("Arial", 20))
word_label.pack(pady=10)

entry = Entry(root)
entry.pack()

Button(root, text="Guess", command=check).pack(pady=10)

lives_label = Label(root, text="Lives: 6")
lives_label.pack()

result_label = Label(root, font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()