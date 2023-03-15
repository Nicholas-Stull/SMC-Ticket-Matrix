import tkinter as tk                                                          
from tkinter import ttk         
import csv           

class Matrix:                   # create class Matrix
    def __init__(self, master): # create init function
        self.master = master    # set master to self.master
        # Create a Frame for the table
        self.categories = []
        with open('src/csv/categories.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.categories.append(row[0])
#----------------------------------------------------------------------------
        self.category_label = ttk.Label(master, text="Select Category:")
        self.category_label.grid(row=0, column=0)

        self.category_var = tk.StringVar()
        self.category_dropdown = ttk.Combobox(
            master, textvariable=self.category_var)
        self.category_dropdown['values'] = self.categories
        self.category_dropdown.grid(row=0, column=1)
        self.category_dropdown.bind(
            '<<ComboboxSelected>>', self.update_dropdown2)

        self.refresh_button = ttk.Button(
            master, text="Refresh", command=self.update_dropdown2)
        self.refresh_button.grid(row=0, column=2, padx=(10, 0))

        # Who Gets The Ticket?
        self.who_gets_the_ticket_button = ttk.Button(
            master, text="Who Gets The Ticket?", command=self.populate_table)
        self.who_gets_the_ticket_button.grid(row=1, column=1)

        self.subcategory_label = ttk.Label(master, text="Select Subcategory:")
        self.subcategory_label.grid(row=1, column=0)

        self.subcategory_var = tk.StringVar()
        self.subcategory_dropdown = ttk.Combobox(
            master, textvariable=self.subcategory_var)
        self.subcategory_dropdown.grid(row=1, column=1)
        self.subcategory_dropdown['values'] = ['']  # default value
        # self.subcategory_dropdown.bind('<<ComboboxSelected>>', self.populate_table)
        self.subcategory_dropdown.bind('<<ComboboxSelected>>')

        self.table_label = ttk.Label(master, text="Table:")
        self.table_label.grid(row=2, column=0)

        self.table = ttk.Treeview(master, columns=('Primary', '2nd', '3rd'))
        self.table.heading('Primary', text='Primary')
        self.table.heading('2nd', text='2nd')
        self.table.heading('3rd', text='3rd')
        self.table.grid(row=3, column=0, columnspan=2)

    def update_dropdown2(self, event=None):
        selected_category = self.category_var.get()
        filename = f'src/csv/{selected_category}.csv'
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                subcategories = [row[0] for row in reader]
        except FileNotFoundError:
            subcategories = ['']  # default value

        self.subcategory_dropdown['values'] = subcategories
        self.subcategory_var.set('')
        self.table.delete(*self.table.get_children())

    def populate_table(self):
        primary = self.subcategory_var.get()
        filename = f'src/csv/{self.category_var.get()}.csv'
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)  # skip the header row
            for row in reader:
                if row[0] == primary:
                    values = row[1].replace('"', '').split(',')
                    self.table.delete(*self.table.get_children())
                    self.table.insert('', 'end', text=primary, values=(
                        primary, values[0], values[1]))


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Matrix 4 : The Matrix Revolutions")
    # root.geometry("400x400")

    # Simply set the theme
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")
    app = Matrix(root)

    # Add a button to populate the table
    populate_button = ttk.Button(
        root, text="Populate Table", command=app.populate_table)
    populate_button.grid(row=4, column=1)

    root.mainloop()
