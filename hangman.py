from os import read
import tkinter as tk
from tkinter import messagebox
import random

# ---------------- WORDS ----------------
with open("words.txt", "r") as file:
    words = file.read().splitlines()
secret_word = random.choice(words)

# ---------------- VARIABLES ----------------
guessed_letters = []
attempts = 6

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Hangman Game")
root.geometry("900x800")
root.config(bg="#121212")
root.resizable(False, False)

# ---------------- TITLE ----------------
title = tk.Label(
    root,
    text="HANGMAN GAME",
    font=("Montserrat", 34, "bold"),
    bg="#121212",
    fg="#00ffcc"
)
title.pack(pady=15)

# ---------------- LOAD IMAGES ----------------
hangman_images = []

for i in range(7):
    img = tk.PhotoImage(file=f"assets/hangman{i}.png")
    hangman_images.append(img)

# ---------------- IMAGE LABEL ----------------
image_label = tk.Label(root, bg="#121212")
image_label.pack()
image_label.pack(pady=10)

# ---------------- WORD LABEL ----------------
word_label = tk.Label(
    root,
    text="",
    font=("Consolas", 32,"bold"),
    bg="#121212",
    fg="white",
)
word_label.pack(pady=20)

# ---------------- ATTEMPTS LABEL ----------------
attempt_label = tk.Label(
    root,
    text=f"Attempts Left: {attempts}",
    font=("Arial", 16,"bold"),
    bg="#121212",
    fg="#ff4d6d"
)
attempt_label.pack()

# ---------------- UPDATE DISPLAY ----------------
def update_display():

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    word_label.config(text=display_word)

    # Update hangman image
    image_label.config(image=hangman_images[6 - attempts])

    # Win condition
    if "_" not in display_word:
        messagebox.showinfo("Hangman", "🎉 You Won!")
        root.destroy()

# ---------------- GUESS FUNCTION ----------------
buttons={}
def guess_letter(letter,button_key):
    global attempts

    btn=buttons[button_key]

    btn.config(state="disabled", bg="#444444", fg="#888888")

    if letter in guessed_letters:
        return

    guessed_letters.append(letter)

    if letter not in secret_word:
        attempts -= 1
        attempt_label.config(text=f"Attempts Left: {attempts}")

    update_display()

    # Lose condition
    if attempts == 0:
        messagebox.showerror(
            "Hangman",
            f"💀 Game Over!\nWord was: {secret_word}"
        )
        root.destroy()

# ---------------- KEYBOARD ----------------
keyboard_frame = tk.Frame(root, bg="#121212")
keyboard_frame.pack(pady=25)

alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM"

row = 0
col = 0

for letter in alphabet:
    btn = tk.Button(
        keyboard_frame,
        text=letter,
        width=4,
        height=2,
        font=("Arial", 12, "bold"),
        bg="#1f1f1f",
        fg="white",
        activebackground="#00ffcc",
        activeforeground="black",
        relief="flat",
        bd=0,
        cursor="hand2",
        command=lambda l=letter.lower(), b=letter: guess_letter(l,b)
    )

    btn.grid(row=row, column=col, padx=3, pady=3)
    buttons[letter]=btn

    col += 1

    if col > 8:
        col = 0
        row += 1

# ---------------- START ----------------
update_display()

root.mainloop()