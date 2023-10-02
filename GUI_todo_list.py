import tkinter as tk
from tkinter import messagebox

# Function to add a task to the to-do list
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to remove a task from the to-do list
def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)

# Function to mark a task as completed
def complete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        task = listbox.get(task_index)
        completed_listbox.insert(tk.END, task)
        listbox.delete(task_index)

# Function to clear the completed tasks
def clear_completed():
    completed_listbox.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Professional To-Do List")

# Create and configure a listbox to display tasks
listbox = tk.Listbox(root, selectmode=tk.SINGLE)
listbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

# Create an entry widget to add tasks
entry = tk.Entry(root, width=40)
entry.pack(padx=20)

# Create buttons to add, remove, complete, and clear tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
complete_button = tk.Button(root, text="Complete Task", command=complete_task)
clear_completed_button = tk.Button(root, text="Clear Completed", command=clear_completed)

add_button.pack(pady=5)
remove_button.pack(pady=5)
complete_button.pack(pady=5)
clear_completed_button.pack(pady=5)

# Create a separate listbox for completed tasks
completed_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
completed_listbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

# Run the GUI application
root.mainloop()
