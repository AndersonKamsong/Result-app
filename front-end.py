import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Dictionary to store student data
students = {
    "Ryan": {"Java": [15, 10], "Merise": [13, 00], "UML": [11, 15], "Maths": [9, 12], "ICT": [15, 2], "Database": [78, 00], "SQL": [18, 19]},
    "Alice": {"Java": [18, 12], "Merise": [10, 7], "UML": [15, 10], "Maths": [9, 8], "ICT": [10, 5], "Database": [2, 18], "SQL": [10, 13]},
    "Bob": {"Java": [2, 5], "Merise": [11, 11], "UML": [10, 15], "Maths": [8, 19], "ICT": [18, 8], "Database": [7, 12], "SQL": [19, 11]},
    "Gaby": {"Java": [12, 8], "Merise": [13, 18], "UML": [10, 11], "Maths": [5, 10], "ICT": [14, 14], "Database": [15, 12], "SQL": [00, 00]}


}

# Function to calculate the average
def calculate_average(student_name):
    student_data = students.get(student_name, {})
    if not student_data:
        return []

    averages = []
    for subject, marks in student_data.items():
        average = (marks[0] + marks[1]) / 2
        averages.append((subject, marks[0], marks[1], average))

    return averages

# Function to display student results in a tabular form
def display_student_result():
    student_name = student_entry.get()
    student_averages = calculate_average(student_name)

    # Clear the table
    for i in tree.get_children():
        tree.delete(i)

    # Display the student results in the table
    for average in student_averages:
        tree.insert("", "end", values=average)

# Function to display all student names
def view_all_students():
    student_names = list(students.keys())
    messagebox.showinfo("Student Names", "\n".join(student_names))

# Main Application Window
root = tk.Tk()
root.title("RESULT APP")
root.geometry("600x400")  # Set initial window size
root.configure(bg='pink')  # Set background color to pink

# Input field for student name
student_label = tk.Label(root, text="Enter Student Name:", bg='pink')
student_label.pack(pady=10)
student_entry = ttk.Entry(root)
student_entry.pack(pady=5)

# Button to display student results
result_button = ttk.Button(root, text="Get Student Results", command=display_student_result)
result_button.pack(pady=10)

# Button to view all student names
view_button = ttk.Button(root, text="View All Students", command=view_all_students)
view_button.pack(pady=10)

# Create a table to display results
tree = ttk.Treeview(root, columns=("Subject", "CA", "SN", "RESULT"), show="headings")
tree.heading("Subject", text="Subject")
tree.heading("CA", text="CA")
tree.heading("SN", text="SN")
tree.heading("RESULT", text="RESULT")
tree.heading("RESULT", text="RESULT")

# Set dimensions of columns
tree.column("Subject", width=100)
tree.column("CA", width=100)
tree.column("SN", width=100)
tree.column("RESULT", width=100)

tree.pack(pady=20)

root.mainloop()
