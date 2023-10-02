import tkinter as tk

# Function to handle button clicks
def click_button(button_text):
    current_text = display_var.get()
    
    if button_text == '=':
        try:
            result = eval(current_text)
            display_var.set(result)
        except Exception as e:
            display_var.set("Error")
    elif button_text == 'C':
        display_var.set("")
    else:
        display_var.set(current_text + button_text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create a StringVar to store and display the calculator input and output
display_var = tk.StringVar()

# Create an Entry widget to display the input and output
display_entry = tk.Entry(root, textvariable=display_var, font=("Helvetica", 18), bd=12, insertwidth=4, width=14, justify='right')
display_entry.grid(row=0, column=0, columnspan=4)

# Define the calculator buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create and arrange the calculator buttons
row, col = 1, 0
for button_text in buttons:
    tk.Button(root, text=button_text, padx=20, pady=20, font=("Helvetica", 18), command=lambda button_text=button_text: click_button(button_text)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the GUI application
root.mainloop()
