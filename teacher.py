import tkinter as tk
from tkinter import messagebox

class TeacherTable:
    def __init__(self, root):
        self.root = root
        self.root.title("Teacher Table")
        self.root.configure(bg="pink")  # Set the background color to pink

        # Create a list to store the teacher data
        self.teachers = []

        # Create labels
        labels = ["ID", "Name", "Subject", "Email", "Password"]
        for i, label in enumerate(labels):
            lbl = tk.Label(root, text=label)
            lbl.grid(row=0, column=i)

        # Create entry fields
        self.id_entry = tk.Entry(root)
        self.name_entry = tk.Entry(root)
        self.subject_entry = tk.Entry(root)
        self.email_entry = tk.Entry(root)
        self.password_entry = tk.Entry(root, show="*")

        self.id_entry.grid(row=1, column=0)
        self.name_entry.grid(row=1, column=1)
        self.subject_entry.grid(row=1, column=2)
        self.email_entry.grid(row=1, column=3)
        self.password_entry.grid(row=1, column=4)

        # Create buttons
        add_btn = tk.Button(root, text="Add", command=self.add_teacher)
        update_btn = tk.Button(root, text="Update", command=self.update_teacher)
        delete_btn = tk.Button(root, text="Delete", command=self.delete_teacher)

        add_btn.grid(row=2, column=0)
        update_btn.grid(row=2, column=1)
        delete_btn.grid(row=2, column=2)

        # Create a listbox to display the teachers
        self.listbox = tk.Listbox(root, width=70)
        self.listbox.grid(row=3, column=0, columnspan=5)

        # Populate the listbox with existing teachers
        self.update_listbox()

    def add_teacher(self):
        teacher_id = self.id_entry.get()
        name = self.name_entry.get()
        subject = self.subject_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Add the teacher to the list
        self.teachers.append((teacher_id, name, subject, email, password))

        # Clear the entry fields
        self.clear_entry_fields()

        # Update the listbox
        self.update_listbox()

    def update_teacher(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            teacher_id = self.id_entry.get()
            name = self.name_entry.get()
            subject = self.subject_entry.get()
            email = self.email_entry.get()
            password = self.password_entry.get()

            # Update the selected teacher in the list
            self.teachers[selected_index[0]] = (teacher_id, name, subject, email, password)

            # Clear the entry fields
            self.clear_entry_fields()

            # Update the listbox
            self.update_listbox()

    def delete_teacher(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            # Delete the selected teacher from the list
            del self.teachers[selected_index[0]]

            # Clear the entry fields
            self.clear_entry_fields()

            # Update the listbox
            self.update_listbox()

    def update_listbox(self):
        # Clear the listbox
        self.listbox.delete(0, tk.END)

        # Populate the listbox with teachers
        for teacher in self.teachers:
            teacher_info = f"ID: {teacher[0]}, Name: {teacher[1]}, Subject: {teacher[2]}, Email: {teacher[3]}, Password: {teacher[4]}"
            self.listbox.insert(tk.END, teacher_info)

    def clear_entry_fields(self):
        # Clear the entry fields
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.subject_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

root = tk.Tk()
teacher_table = TeacherTable(root)
root.mainloop()