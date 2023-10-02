import tkinter as tk
import random

# Function to determine the winner of the game
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Scissors" and computer_choice == "Paper") or
        (user_choice == "Paper" and computer_choice == "Rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle user choice and update the game
def play_game(user_choice):
    computer_choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(computer_choices)

    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Computer chose {computer_choice}. {result}")

    update_scores(result)

# Function to update scores
def update_scores(result):
    global user_score, computer_score
    if "You win" in result:
        user_score += 1
    elif "Computer wins" in result:
        computer_score += 1

    score_label.config(text=f"User: {user_score}  |  Computer: {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score, computer_score = 0, 0
    score_label.config(text="User: 0  |  Computer: 0")
    result_label.config(text="Choose Rock, Paper, or Scissors:")

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Create a label for instructions
instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Helvetica", 14))
instruction_label.pack(pady=10)

# Create buttons for user choices
choices = ["Rock", "Paper", "Scissors"]
for choice in choices:
    tk.Button(root, text=choice, padx=20, pady=10, font=("Helvetica", 14), command=lambda choice=choice: play_game(choice)).pack(padx=10)

# Create a label to display the game result
result_label = tk.Label(root, text="Ready to play?", font=("Helvetica", 16))
result_label.pack(pady=20)

# Create a label to display the score
user_score, computer_score = 0, 0
score_label = tk.Label(root, text="User: 0  |  Computer: 0", font=("Helvetica", 14))
score_label.pack()

# Create a button to reset the game
reset_button = tk.Button(root, text="Play Again", padx=20, pady=10, font=("Helvetica", 14), command=reset_game)
reset_button.pack(pady=20)

# Run the GUI application
root.mainloop()
