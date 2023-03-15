import tkinter as tk
from tkinter import ttk
import csv
#----------------------------------------------------------------------


class Matrix(ttk.Frame, object):
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        # Make the app responsive
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)

        # Create a Frame for input widgets
        self.widgets_frame = ttk.Frame(self, padding=(0, 0, 0, 10))
        self.widgets_frame.grid(
            row=0, column=0, padx=10, pady=(30, 10), sticky="nsew", rowspan=6
        )
        self.widgets_frame.columnconfigure(index=0, weight=1)
        self.categories = []
        with open('src/csv/categories.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.categories.append(row[0])


# ----------------------------------------------------------------------
        # Cat Label
        self.cat_label = ttk.Label(
            self.widgets_frame, text="Select Category:")
        self.cat_label.grid(
            row=0, column=0, padx=5, pady=(0, 10), sticky="ew")
        

#----------------------------------------------------------------------
        # Cat Entry
        self.cat_var = tk.StringVar()
        self.cat_drop = ttk.Combobox(textvariable=self.cat_var)
        self.cat_drop.grid(row=0, column=1, padx=5,  sticky="ew")
        self.cat_drop['values'] = self.categories
        self.cat_drop.bind(
            '<<ComboboxSelected>>', self.update_dropdown2)
#----------------------------------------------------------------------
        # SubCat Label
        self.subcategory_label = ttk.Label(text="Select Subcategory:")
        self.subcategory_label.grid(
            row=1, column=0, padx=5, pady=(0, 10), sticky="ew")

        self.Matrix_Table = ttk.Treeview(self, columns=('Primary', '2nd', '3rd'))
        self.Matrix_Table.grid(row=2, column=0, columnspan=2)
        self.Matrix_Table.heading('Primary', text='Primary')
        self.Matrix_Table.heading('2nd', text='2nd')
        self.Matrix_Table.heading('3rd', text='3rd')
        

    def check_eligibility(self):
        try:
            # Retrieve values from entries
            first_name = self.fname.get()
            last_name = self.lname.get()
            major = self.major.get()
            credits = int(self.credits.get())

            # Check eligibility based on criteria
            if credits >= 125 and major.lower() == "it":
                message = f"Congratulations {first_name} {last_name}.\nYou are eligible for an internship!\nThe Minimum credits for the internship is 125"
            else:
                message = f"Sorry {first_name} {last_name}.\nYou are not eligible for an internship.\nThe Minimum credits for the internship is 125"

            # Display result
            self.results.config(text=message)

        except ValueError:
            # Handle ValueError if credits is not an integer
            self.results.config(text="Credits must be an integer.")

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

if __name__ == "__main__":
    root = tk.Tk()
    root.title("SMC Ticket Matrix   ")
    # root.geometry("400x400")

    # Simply set the theme
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")

    app = Matrix(root)
    app.grid(row=0, column=0, sticky="nsew")

    # Set a minsize for the window, and place it in the middle

    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) -
                      (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) -
                      (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

    root.mainloop()
