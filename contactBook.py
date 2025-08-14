import tkinter as tk
from tkinter import messagebox, simpledialog

contacts = []  # Store contacts as dictionaries

def refresh_listbox():
    """Update the Listbox with names + phone numbers."""
    listbox.delete(0, tk.END)
    for idx, contact in enumerate(contacts, start=1):
        listbox.insert(tk.END, f"{idx}. {contact['name']} - {contact['phone']}")

def add_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()
    address = entry_address.get().strip()

    if name and phone:
        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        clear_entries()
        refresh_listbox()
    else:
        messagebox.showwarning("Warning", "Name and Phone are required.")

def delete_contact():
    try:
        index = listbox.curselection()[0]
        contacts.pop(index)
        refresh_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Select a contact to delete.")

def search_contact():
    keyword = simpledialog.askstring("Search Contact", "Enter name or phone number:")
    if keyword:
        results = [c for c in contacts if keyword.lower() in c['name'].lower() or keyword in c['phone']]
        if results:
            listbox.delete(0, tk.END)
            for idx, contact in enumerate(results, start=1):
                listbox.insert(tk.END, f"{idx}. {contact['name']} - {contact['phone']}")
        else:
            messagebox.showinfo("Search", "No matching contacts found.")

def update_contact():
    try:
        index = listbox.curselection()[0]
        contact = contacts[index]

        name = simpledialog.askstring("Update Name", "Enter new name:", initialvalue=contact['name'])
        phone = simpledialog.askstring("Update Phone", "Enter new phone:", initialvalue=contact['phone'])
        email = simpledialog.askstring("Update Email", "Enter new email:", initialvalue=contact['email'])
        address = simpledialog.askstring("Update Address", "Enter new address:", initialvalue=contact['address'])

        if name and phone:
            contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
            refresh_listbox()
        else:
            messagebox.showwarning("Warning", "Name and Phone are required.")
    except IndexError:
        messagebox.showwarning("Warning", "Select a contact to update.")

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

def view_contact_details(event):
    """Show full details of a contact when double-clicked."""
    try:
        index = listbox.curselection()[0]
        contact = contacts[index]
        details = (
            f"Name: {contact['name']}\n"
            f"Phone: {contact['phone']}\n"
            f"Email: {contact['email']}\n"
            f"Address: {contact['address']}"
        )
        messagebox.showinfo("Contact Details", details)
    except IndexError:
        pass  # Ignore if double-click happens without a selection

# --- GUI Setup ---
root = tk.Tk()
root.title("Contact Book")
root.geometry("450x500")
root.config(bg="#f7f7f7")

tk.Label(root, text="📇 Contact Book", font=("Arial", 18, "bold"), bg="#f7f7f7").pack(pady=10)

# Input Fields
form_frame = tk.Frame(root, bg="#f7f7f7")
form_frame.pack(pady=5)

tk.Label(form_frame, text="Name:", bg="#f7f7f7").grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(form_frame, font=("Arial", 12), width=30)
entry_name.grid(row=0, column=1, pady=2)

tk.Label(form_frame, text="Phone:", bg="#f7f7f7").grid(row=1, column=0, sticky="w")
entry_phone = tk.Entry(form_frame, font=("Arial", 12), width=30)
entry_phone.grid(row=1, column=1, pady=2)

tk.Label(form_frame, text="Email:", bg="#f7f7f7").grid(row=2, column=0, sticky="w")
entry_email = tk.Entry(form_frame, font=("Arial", 12), width=30)
entry_email.grid(row=2, column=1, pady=2)

tk.Label(form_frame, text="Address:", bg="#f7f7f7").grid(row=3, column=0, sticky="w")
entry_address = tk.Entry(form_frame, font=("Arial", 12), width=30)
entry_address.grid(row=3, column=1, pady=2)

# Buttons
btn_frame = tk.Frame(root, bg="#f7f7f7")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", command=add_contact, bg="#4CAF50", fg="white", width=10).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update", command=update_contact, bg="#2196F3", fg="white", width=10).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", command=delete_contact, bg="#F44336", fg="white", width=10).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Search", command=search_contact, bg="#FFC107", fg="black", width=10).grid(row=1, column=1, padx=5, pady=5)

# Listbox
listbox = tk.Listbox(root, font=("Arial", 12), width=50, height=12, bd=2, relief="solid", selectbackground="#d1e7dd")
listbox.pack(pady=10)

# Bind double-click to view contact details
listbox.bind("<Double-1>", view_contact_details)

root.mainloop()
