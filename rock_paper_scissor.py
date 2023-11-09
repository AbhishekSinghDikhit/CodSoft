import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import random

def play_game(player_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    result_label.config(text=f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        outcome_label.config(text="It's a tie!")
    elif (
        (player_choice == 'Rock' and computer_choice == 'Scissors') or
        (player_choice == 'Paper' and computer_choice == 'Rock') or
        (player_choice == 'Scissors' and computer_choice == 'Paper')
    ):
        outcome_label.config(text="You win!", foreground='darkgreen')
    else:
        outcome_label.config(text="You lose!", foreground='red')

    play_again_button.pack()

def reset_game():
    result_label.config(text="")
    outcome_label.config(text="", foreground='black')
    play_again_button.pack_forget()
    
def on_exit():
    result = messagebox.showinfo("Thank You!", "Thank you for Playing")
    if result == "ok":
        root.destroy()

# Create the main window
root = tk.Tk()
root.geometry('420x430')
root.resizable(False, False)
root.configure(bg='lightgreen')
root.title("Rock Paper Scissors Game")


label = tk.Label(root, text="ROCK, PAPER & SCISSORS", font=("Helvetica", 14, 'bold'))
label.configure(fg='black', bg='lightgreen')
label.pack(pady=10)

# Create buttons for Rock, Paper, and Scissors
rock_button = tk.Button(root, text="Rock", relief='raised',command=lambda: play_game('Rock'), width=7, height=1, font="Roboto 14 bold", bg="brown", fg="white", cursor='hand2')
rock_button.pack(padx=5, pady=10)

paper_button = tk.Button(root, text="Paper", relief='raised',command=lambda: play_game('paper'), width=7, height=1, font="Roboto 14 bold", bg="white", fg="black", cursor='hand2')
paper_button.pack(padx=7,pady=10)

scissors_button = tk.Button(root, text="Scissors", relief='raised',command=lambda: play_game('Scissors'), width=7, height=1, font="Roboto 14 bold", bg="gray", fg="black", cursor='hand2')
scissors_button.pack(padx=9, pady=10)

# Create labels for result and outcome
result_label = ttk.Label(root, text="", font=('Arial', 12, 'italic', 'bold'))
result_label.configure(background='orange', relief='raised')
result_label.pack()

outcome_label = ttk.Label(root, text="", font=('Arial', 14, 'bold'))
outcome_label.configure(background='yellow', border=7, relief='solid')
outcome_label.pack()

# Create "Play Again" button
play_again_button = tk.Button(root, text="Play Again", width='10', bg='lightgreen', fg='black', relief='solid',font="Roboto 12 bold", command=reset_game, cursor='hand2')

exit_button = tk.Button(root, text="Exit", bg='red', fg='black', relief='solid',font="Roboto 12 bold", command=on_exit, cursor='hand2')
exit_button.pack(pady=10)
# Run the Tkinter event loop
root.mainloop()