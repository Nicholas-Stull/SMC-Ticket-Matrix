import tkinter as tk
from tkinter import ttk
import csv
# ----------------------------------------------------------------------


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
            row=0, column=1, padx=10, pady=(30, 10), sticky="nsew"
        )
        self.widgets_frame.columnconfigure(index=0, weight=1)

        # Create a Frame for the table
        self.table_frame = ttk.Frame(self, padding=(0, 0, 0, 10))
        self.table_frame.grid(
            row=0, column=0, padx=10, pady=(30, 10), sticky="nsew"
        )
        self.table_frame.columnconfigure(index=0, weight=1)
        self.table_frame.rowconfigure(index=0, weight=1)

        # Create the table
        self.table = ttk.Treeview(self.table_frame, columns=("0", "1", "2"))
        self.table.grid(row=0, column=0, sticky="nsew")
        self.table.heading("0", text="Primary")
        self.table.heading("1", text="Secondary")
        self.table.heading("2", text="Third/Anyone of These")
        self.table.columnconfigure(index=0, weight=1)
        self.table.columnconfigure(index=1, weight=1)
        self.table.columnconfigure(index=2, weight=1)
        self.table.rowconfigure(index=0, weight=1)

        # Create the labels and dropdowns
        self.cat_label = ttk.Label(self.widgets_frame, text="Category:")
        self.cat_label.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="w")
        self.cat_var = tk.StringVar()
        self.cat_drop = ttk.Combobox(
            self.widgets_frame, textvariable=self.cat_var)
        self.cat_drop.grid(row=1, column=0, padx=5, pady=(0, 10), sticky="ew")
        self.cat_drop["values"] = ["Option 1", "Option 2", "Option 3"]
        self.cat_drop.bind("<<ComboboxSelected>>", self.update_dropdown2)

        self.subcat_label = ttk.Label(self.widgets_frame, text="Sub-Category:")
        self.subcat_label.grid(row=2, column=0, padx=5,
                               pady=(0, 10), sticky="w")
        self.subcat_var = tk.StringVar()
        self.subcat_drop = ttk.Combobox(
            self.widgets_frame, textvariable=self.subcat_var
        )
        self.subcat_drop.grid(row=3, column=0, padx=5,
                              pady=(0, 10), sticky="ew")
        self.subcat_drop["values"] = ["Option A", "Option B", "Option C"]
        self.subcat_drop.bind("<<ComboboxSelected>>", self.update_dropdown2)

        # Create the refresh and ticket buttons
        self.refresh_button = ttk.Button(
            self.widgets_frame, text="Refresh", command=self.refresh_table
        )
        self.refresh_button.grid(
            row=4, column=0, padx=5, pady=(0, 10), sticky="ew")

        # Whose Ticket Button
        self.whose_ticket_button = ttk.Button(
            self.widgets_frame, text="Whose Ticket Is It Anyway?", command=self.show_whose_ticket)
        self.whose_ticket_button.grid(
            row=5, column=0, padx=5, pady=(0, 10), sticky="e")

    def refresh_table(self):
        # Code to refresh the table goes here
        pass

    def show_whose_ticket(self):
        # Code to show whose ticket it is goes here
        pass

# ...



    
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
