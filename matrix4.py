import tkinter as tk
from tkinter import ttk
import csv


class Matrix:
    def __init__(self, master):
        self.master = master
        
        
        self.categories = []
        with open('src/csv/categories.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.categories.append(row[0])
        
        self.category_label = ttk.Label(master, text="Select Category:")
        self.category_label.grid(row=0, column=0)
        
        self.category_var = tk.StringVar()
        self.category_dropdown = ttk.Combobox(master, textvariable=self.category_var)
        self.category_dropdown['values'] = self.categories
        self.category_dropdown.grid(row=0, column=1)
        self.category_dropdown.bind('<<ComboboxSelected>>', self.update_dropdown2)
        
        self.refresh_button = ttk.Button(master, text="Refresh", command=self.update_dropdown2)
        self.refresh_button.grid(row=0, column=2, padx=(10,0))
        
        # Who Gets The Ticket?
        #self.who_gets_the_ticket_button = ttk.Button(
        #    master, text="Who Gets The Ticket?", command=self.WhoGetsTheTicket)
        
        self.subcategory_label = ttk.Label(master, text="Select Subcategory:")
        self.subcategory_label.grid(row=1, column=0)
        
        self.subcategory_var = tk.StringVar()
        self.subcategory_dropdown = ttk.Combobox(master, textvariable=self.subcategory_var)
        self.subcategory_dropdown.grid(row=1, column=1)
        self.subcategory_dropdown['values'] = ['']  # default value
        #self.subcategory_dropdown.bind('<<ComboboxSelected>>', self.populate_table)
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
                data = [row for row in reader]
                subcategories = [row[0] for row in data]
        except FileNotFoundError:
            subcategories = ['']  # default value

        self.subcategory_dropdown['values'] = subcategories
        self.subcategory_var.set('')
        self.table.delete(*self.table.get_children())

        # populate the table with data for the selected subcategory
        selected_subcategory = self.subcategory_var.get()
        if selected_subcategory:
            for row in data:
                if row[0] == selected_subcategory:
                    # create a list of people from the csv row
                    people = [p.strip() for p in row[1].strip('"').split(',')]
                    # insert the row data into the table
                    self.table.insert(
                        '', 'end', text=row[0], values=(row[0], people))



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Matrix 4 : The Matrix Revolutions")
    # root.geometry("400x400")

    # Simply set the theme
    #root.tk.call("source", "azure.tcl")
    #root.tk.call("set_theme", "dark")
    app = Matrix(root)

    root.mainloop()