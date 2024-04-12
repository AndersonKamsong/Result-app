
import customtkinter
import tkinter.ttk as ttk

class CourseView(customtkinter.CTkFrame):

    def __init__(self, parent, title=""):
        super().__init__(parent)  # Call the parent class constructor
        self.coursePanel_frame = customtkinter.CTkScrollableFrame(parent, height=850,width=950)
        self.coursePanel_frame.grid(row=0, column=1, padx=(10, 0), pady=(10, 0), sticky="nsew")
        if title:
            self.logo_label = customtkinter.CTkLabel(self.coursePanel_frame, text=title,
                                                     font=customtkinter.CTkFont(size=20, weight="bold"))
            self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        # Create the table (Treeview)
        self.table = ttk.Treeview(master=self.coursePanel_frame, columns=("Column 1", "Column 2", "Column 3"))

        # Define column headings
        self.table.heading("#0", text="ID")  # Optional for automatic row numbering
        self.table.heading("Column 1", text="Column 1 Text")
        self.table.heading("Column 2", text="Column 2 Text")
        self.table.heading("Column 3", text="Column 3 Text")

        # Set column widths (optional)
        self.table.column("#0", width=50)  # Adjust widths as needed
        self.table.column("Column 1", width=150)
        self.table.column("Column 2", width=150)
        self.table.column("Column 3", width=150)

        # Show table headings (optional)
        # self.table.show("headings")

        # Insert some sample data
        self.table.insert("", 1, values=("1", "Data 1.1", "Data 1.2", "Data 1.3"))
        self.table.insert("", 2, values=("2", "Data 2.1", "Data 2.2", "Data 2.3"))

        # Pack the table into the main frame
        # self.table.pack(fill=ttk.BOTH, expand=True)
