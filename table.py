import tkinter as tk
from tkinter import ttk
from rx.subject import Subject
class Observable:
    def __init__(self):
        self.subject = Subject()

    def subscribe(self, callback):
        return self.subject.subscribe(callback)

    def notify(self, data):
        self.subject.on_next(data)

class Student:
    def __init__(self, matricule, name, ca_mark, sn_mark, reseat_mark):
        self.matricule = matricule
        self.name = name
        self.ca_mark = ca_mark
        self.sn_mark = sn_mark
        self.reseat_mark = reseat_mark

class StudentViewModel:
    def __init__(self):
        self.students = []
        self.students_changed = Observable()

    def add_student(self, matricule, name, ca_mark, sn_mark, reseat_mark):
        student = Student(matricule, name, ca_mark, sn_mark, reseat_mark)
        self.students.append (student)
        self.students_changed.notify(self.students)

        # Inside the StudentViewModel class

def get_student_by_id(self, student_id):
    for student in self.students:
        if student.matricule == student_id:
            return student
    return None

class TableView:
    def __init__(self, root, view_model):
        self.root = root
        self.view_model = view_model

        self.table = ttk.Treeview(root)
        self.table["columns"] = ("Matricule", "Name", "CA Mark", "SN Mark", "Reseat Mark")
        self.table.column("#0", width=0, stretch=tk.NO)
        self.table.column("Matricule", anchor=tk.CENTER, width=100)
        self.table.column("Name", anchor=tk.CENTER, width=150)
        self.table.column("CA Mark", anchor=tk.CENTER, width=100)
        self.table.column("SN Mark", anchor=tk.CENTER, width=100)
        self.table.column("Reseat Mark", anchor=tk.CENTER, width=100)

        self.table.heading("#0", text="")
        self.table.heading("Matricule", text="Matricule")
        self.table.heading("Name", text="Name")
        self.table.heading("CA Mark", text="CA Mark")
        self.table.heading("SN Mark", text="SN Mark")
        self.table.heading("Reseat Mark", text="Reseat Mark")

        self.table.tag_configure("oddrow", background="red")
        self.table.tag_configure("evenrow", background="red")


        self.table.pack()

        self.view_model.students_changed.subscribe(self.update_table)

    def update_table(self, students):
        self.table.delete(*self.table.get_children())

        for student in students:
            self.table.insert("", tk.END, text="",
                              values=(student.matricule, student.name, student.ca_mark, student.sn_mark, student.reseat_mark,))

                    # Inside the TableView class

def update_student(self, updated_matricule, updated_name, updated_ca_mark, updated_sn_mark, updated_reseat_mark):
    if self.selected_student:
        self.selected_student.matricule = updated_matricule
        self.selected_student.name = updated_name
        self.selected_student.ca_mark = updated_ca_mark
        self.selected_student.sn_mark = updated_sn_mark
        self.selected_student.reseat_mark = updated_reseat_mark
        self.view_model.students_changed.notify(self.view_model.students)
        # Close the editing interface or clear the input fields

# Rest of the code...
class AppView:
    def __init__(self, root, view_model):
        self.root = root
        self.view_model = view_model

        self.matricule_entry = ttk.Entry(root)
        self.matricule_entry.pack()

        self.name_entry = ttk.Entry(root)
        self.name_entry.pack()

        self.ca_mark_entry = ttk.Entry(root)
        self.ca_mark_entry.pack()

        self.sn_mark_entry = ttk.Entry(root)
        self.sn_mark_entry.pack()

        self.reseat_mark_entry = ttk.Entry(root)
        self.reseat_mark_entry.pack()

        self.add_button = ttk.Button(root, text="Add", command=self.add_student)
        self.add_button.pack()

    def add_student(self):
        matricule = self.matricule_entry.get()
        name = self.name_entry.get()
        ca_mark = self.ca_mark_entry.get()
        sn_mark = self.sn_mark_entry.get()
        reseat_mark = self.reseat_mark_entry.get()

        self.view_model.add_student(matricule, name, ca_mark, sn_mark, reseat_mark,)

def main():
    root = tk.Tk()
    root.title("Student Table")

    view_model = StudentViewModel()

    table_view = TableView(root, view_model)
    app_view = AppView(root, view_model)

    root.mainloop()

if __name__ == "__main__":
    main()