import tkinter as tk
import random
import string
import sys
import os

def click_letter(letter):
    clicked_letters.append(letter)
    label.config(text=f"Clicked letters: {' '.join(clicked_letters)}", fg="white")

def clear_letters():
    global clicked_letters
    clicked_letters = []
    label.config(text="Clicked letters:", fg="white")
    label_word.config(text="Formed word:", fg="white")
    label_search_result.config(text="", fg="white")

def create_word():
    word = ''.join(clicked_letters)
    label_word.config(text=f"Formed word: {word}", fg="white")
    search_word(word)

def search_word(pattern):
    found = False
    with open('text.txt', 'r') as file:
        for line in file:
            if star_search(pattern.lower(), line.lower()):
                label_search_result.config(text=f"Found: {line.strip()}", fg="green")
                found = True
                if line.strip() not in found_words:
                    found_words.append(line.strip())
                break
    if not found:
        label_search_result.config(text="Not found", fg="red")
    update_found_words_label()

def update_found_words_label():
    label_found_words.config(text=f"Found words: {' '.join(found_words)}", fg="white")

def star_search(pattern, text):
    if not pattern:
        return True
    if not text:
        return False
    if pattern[0] == '*':
        return star_search(pattern[1:], text) or star_search(pattern, text[1:])
    else:
        return (pattern[0] == text[0]) and star_search(pattern[1:], text[1:])

def generate_letters():
    global letters, found_words
    letters = random.choices(string.ascii_uppercase, k=20)
    for btn, letter in zip(buttons, letters):
        btn.config(text=letter)
    clicked_letters.clear()
    label.config(text="Clicked letters:", fg="white")
    label_word.config(text="Formed word:", fg="white")
    label_search_result.config(text="", fg="white")
    found_words.clear()
    update_found_words_label()

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

letters = random.choices(string.ascii_uppercase, k=20)

root = tk.Tk()
root.title("!!!Бүх үгийг олоорой!!!")
root.configure(bg="black")

label = tk.Label(root, text="", font=("Arial", 16), fg="white", bg="black")
label.grid(row=0, column=7, columnspan=7, pady=20)

clicked_letters = []
buttons = []
col = 0
for letter in letters:
    btn = tk.Button(root, text=letter, command=lambda l=letter: click_letter(l), padx=10, pady=5, font=("Arial", 12), bg="gray", fg="white", width=3)
    btn.grid(row=1, column=col, padx=5, pady=5)
    buttons.append(btn)
    col += 1

done_btn = tk.Button(root, text="Done", command=create_word, padx=160, pady=5, font=("Arial", 12), bg="green", fg="white")
done_btn.grid(row=2, column=0, columnspan=7, pady=0)

clear_btn = tk.Button(root, text="Clear", command=clear_letters, padx=160, pady=5, font=("Arial", 12), bg="red", fg="white")
clear_btn.grid(row=2, column=7, columnspan=6, pady=0)

refresh_btn = tk.Button(root, text="Refresh", command=generate_letters, padx=160, pady=5, font=("Arial", 12), bg="blue", fg="white")
refresh_btn.grid(row=2, column=13, columnspan=7, pady=0)

label_word = tk.Label(root, text="Created:", font=("Arial", 16), fg="white", bg="black")
label_word.grid(row=3, column=7, columnspan=7, pady=20)

label_search_result = tk.Label(root, text="", font=("Arial", 14), fg="white", bg="black")
label_search_result.grid(row=4, column=7, columnspan=7, pady=20)

found_words = []
label_found_words = tk.Label(root, text="List:", font=("Arial", 16), fg="white", bg="black")
label_found_words.grid(row=5, column=7, columnspan=7, pady=20)

root.mainloop()
