import tkinter as tk
import random
import string

def generate_password():
    length = int(password_length.get())
    if length < 1:
        password_result.set("Invalid length")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_result.set(password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Calculate the center of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 400
window_height = 250
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Set the window size and position
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a label for instructions
instruction_label = tk.Label(root, text="Enter password length:", font=("Helvetica", 16))
instruction_label.pack(pady=20)

# Create an entry field for password length input
password_length = tk.Entry(root, font=("Helvetica", 16))
password_length.pack()

# Create a button to generate the password
generate_button = tk.Button(root, text="Generate Password", font=("Helvetica", 16), command=generate_password)
generate_button.pack(pady=20)

# Create a label to display the generated password
password_result = tk.StringVar()
password_result_label = tk.Label(root, textvariable=password_result, font=("Helvetica", 16))
password_result_label.pack()

# Run the GUI application
root.mainloop()
