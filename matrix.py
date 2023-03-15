import tkinter as tk
from tkinter import ttk
import csv

class App:
    def __init__(self, master):
        self.master = master
        master.title("Dropdown Example")
        
        # Read data from CSV file
        self.categories = []
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.categories.append(row)
        
        self.category_label = ttk.Label(master, text="Select Category:")
        self.category_label.grid(row=0, column=0)
        
        self.category_var = tk.StringVar()
        self.category_dropdown = ttk.Combobox(master, textvariable=self.category_var)
        self.category_dropdown['values'] = [row[0] for row in self.categories]
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
        for row in self.categories:
            if row[0] == selected_category:
                subcategories = row[1:]
                break
        else:
            subcategories = ['']  # default value
        
        self.subcategory_dropdown['values'] = subcategories
        self.subcategory_var.set('')
        self.table.delete(*self.table.get_children())
    
    def populate_table(self, event):
        primary = self.subcategory_var.get()
        second = 'Second'
        third = 'Third'
        
        self.table.insert('', 'end', text=primary, values=(primary, second, third))

root = tk.Tk()
app = App(root)
root.mainloop()
