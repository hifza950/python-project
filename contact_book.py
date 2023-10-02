import tkinter as tk
from tkinter import messagebox

# Create a list to store contacts (each contact is a dictionary)
contacts = []

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contact = {
            "Name": name,
            "Phone": phone,
            "Email": email,
            "Address": address
        }
        contacts.append(contact)
        clear_entries()
        update_contact_list()
        messagebox.showinfo("Success", "Contact added successfully.")
    else:
        messagebox.showerror("Error", "Name and Phone fields are required.")

# Function to update the contact list display
def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, contact["Name"] + " - " + contact["Phone"])

# Function to search for a contact
def search_contact():
    query = search_entry.get().lower()
    search_result = []
    for contact in contacts:
        if query in contact["Name"].lower() or query in contact["Phone"]:
            search_result.append(contact["Name"] + " - " + contact["Phone"])
    if search_result:
        contact_listbox.delete(0, tk.END)
        for result in search_result:
            contact_listbox.insert(tk.END, result)
    else:
        messagebox.showinfo("Not Found", "No matching contacts found.")

# Function to clear input fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)

# Function to view contact details
def view_contact():
    selected_contact = contact_listbox.curselection()
    if selected_contact:
        index = selected_contact[0]
        contact_details = contacts[index]
        messagebox.showinfo(
            "Contact Details",
            f"Name: {contact_details['Name']}\nPhone: {contact_details['Phone']}\nEmail: {contact_details['Email']}\nAddress: {contact_details['Address']}"
        )
    else:
        messagebox.showinfo("No Selection", "Please select a contact.")

# Function to update contact details
def update_contact():
    selected_contact = contact_listbox.curselection()
    if selected_contact:
        index = selected_contact[0]
        new_name = name_entry.get()
        new_phone = phone_entry.get()
        new_email = email_entry.get()
        new_address = address_entry.get()

        if new_name and new_phone:
            contacts[index]["Name"] = new_name
            contacts[index]["Phone"] = new_phone
            contacts[index]["Email"] = new_email
            contacts[index]["Address"] = new_address
            clear_entries()
            update_contact_list()
            messagebox.showinfo("Success", "Contact updated successfully.")
        else:
            messagebox.showerror("Error", "Name and Phone fields are required.")
    else:
        messagebox.showinfo("No Selection", "Please select a contact.")

# Function to delete a contact
def delete_contact():
    selected_contact = contact_listbox.curselection()
    if selected_contact:
        index = selected_contact[0]
        contacts.pop(index)
        update_contact_list()
        messagebox.showinfo("Success", "Contact deleted successfully.")
    else:
        messagebox.showinfo("No Selection", "Please select a contact.")

# Create the main window
root = tk.Tk()
root.title("Contact Management")

# Create labels and entry fields for contact details
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

phone_label = tk.Label(root, text="Phone:")
phone_label.grid(row=1, column=0, padx=10, pady=5)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

email_label = tk.Label(root, text="Email:")
email_label.grid(row=2, column=0, padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=10, pady=5)

address_label = tk.Label(root, text="Address:")
address_label.grid(row=3, column=0, padx=10, pady=5)
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1, padx=10, pady=5)

# Create buttons for actions
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=0, column=2, padx=10, pady=5)

update_button = tk.Button(root, text="Update Contact", command=update_contact)
update_button.grid(row=1, column=2, padx=10, pady=5)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=2, column=2, padx=10, pady=5)

search_label = tk.Label(root, text="Search:")
search_label.grid(row=4, column=0, padx=10, pady=5)
search_entry = tk.Entry(root)
search_entry.grid(row=4, column=1, padx=10, pady=5)

search_button = tk.Button(root, text="Search", command=search_contact)
search_button.grid(row=4, column=2, padx=10, pady=5)

view_button = tk.Button(root, text="View Contact", command=view_contact)
view_button.grid(row=5, column=1, padx=10, pady=5)

# Create a listbox to display contacts
contact_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=15)
contact_listbox.grid(row=6, column=0, columnspan=3, padx=10, pady=5)

# Initialize the contact list display
update_contact_list()

# Run the GUI application
root.mainloop()
