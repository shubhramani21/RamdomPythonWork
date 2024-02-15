import tkinter as tk
import random

def check_guess():
    user_guess = int(entry.get())
    result = "Correct!" if user_guess == computer else "Incorrect!"
    result_label.config(text=result)
    actual_label.config(text=f"Actual number: {computer}")
    user_label.config(text=f"Your number: {user_guess}")

# Set up the Tkinter window
root = tk.Tk()
root.title("Number Guessing Game")

# Generate a random number between 1 and 10
computer = random.randint(1, 10)

# Create and place widgets
instruction_label = tk.Label(root, text="Guess a number between 1 and 10:")
instruction_label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

guess_button = tk.Button(root, text="Check Guess", command=check_guess)
guess_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

actual_label = tk.Label(root, text="")
actual_label.pack()

user_label = tk.Label(root, text="")
user_label.pack()

# Run the Tkinter event loop
root.mainloop()
