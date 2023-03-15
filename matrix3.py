import tkinter as tk
from tkinter import ttk
import csv

class App:
    def __init__(self, master):
        self.master = master
        master.title("Dropdown Example")
        
        # Read categories from Categories.csv file
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
        
        self.subcategory_label = ttk.Label(master, text="Select Subcategory:")
        self.subcategory_label.grid(row=1, column=0)
        
        self.subcategory_var = tk.StringVar()
        self.subcategory_dropdown = ttk.Combobox(master, textvariable=self.subcategory_var)
        self.subcategory_dropdown.grid(row=1, column=1)
        self.subcategory_dropdown['values'] = ['']  # default value
        self.subcategory_dropdown.bind('<<ComboboxSelected>>', self.populate_table)
        
        self.table_label = ttk.Label(master, text="Table:")
        self.table_label.grid(row=2, column=0)
        
        self.table = ttk.Treeview(master, columns=('Primary', '2nd', '3rd'))
        self.table.heading('Primary', text='Primary')
        self.table.heading('2nd', text='2nd')
        self.table.heading('3rd', text='3rd')
        self.table.grid(row=3, column=0, columnspan=2)
    
    def update_dropdown2(self, event):
        selected_category = self.category_var.get()
        lowercase_category = selected_category.lower()
        csv_file = f'src/csv/{lowercase_category}.csv'
        try:
            with open(csv_file, 'r') as file:
                reader = csv.reader(file)
                subcategories = next(reader)
        except FileNotFoundError:
            subcategories = ['']  # default value
        
        self.subcategory_dropdown['values'] = subcategories
        self.subcategory_var.set('')
        self.table.delete(*self.table.get_children())
    
    def populate_table(self, event):
        selected_category = self.category_var.get()
        selected_subcategory = self.subcategory_var.get()
        csv_file = selected_category + ".csv"
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # skip header row
            for row in reader:
                if row[0] == selected_subcategory:
                    primary = row[1].split(",")
                    second = row[2].split(",")
                    third = row[3].split(",")
                    break
            else:
                primary = []
                second = []
                third = []
        
        for p, s, t in zip(primary, second, third):
            self.table.insert('', 'end', text=p, values=(p, s, t))

root = tk.Tk()
app = App(root)
root.mainloop()
