import tkinter as tk
from tkinter import ttk
from tkinter import *
import csv


def update_category_dropdown():
    # Load the categories from the CSV file
    maincat = 'src/csv/categories.csv'
    with open(maincat, encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        # next(reader)  # Skip header row
        categories = [row[0] for row in reader]

    # Update the dropdown list with the categories
    category_dropdown['values'] = categories
    category_dropdown.current(0)  # Set default selection


def update_listbox(*args):
    # Load the data from the selected category file
    cat_picked = category_var.get()
    filename = f'src/csv/{cat_picked}.csv'
    strippedcat = filename.replace(" ", "").lower()
    with open(strippedcat, encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        data = list(reader)

    # Clear the labels
    catset2.config(text="")
    prim2.config(text="")
    sec2.config(text="")
    tri2.config(text="")

    # Update the Listbox with the data
    var.set([row[0] for row in data])

    # Get the selected row and update the labels with its data
    try:
        selected_row = data[listbox1.curselection()[0]]
        catset2.config(text=selected_row[0])
        prim2.config(text=selected_row[1])
        sec2.config(text=selected_row[2])
        tri2.config(text=selected_row[3])
    except IndexError:
        pass


# Set up the GUI
root = Tk()
root.geometry('380x320')
# Create a canvas to hold the image and header
canvas = tk.Canvas(root, width=200, height=50)
canvas.grid(row=0, column=1, sticky='ne')

# Load the image and add it to the canvas
# sets the image paths to easily change them later
smc_logo = './src/images/smc-logo.png'
smc_seal = './src/images/smc-seal.png'


img = PhotoImage(file=smc_seal)
img = img.subsample(4)  # resize the image to 1/4 of its original size
canvas.create_image(0, 0, anchor='nw', image=img)
canvas.grid(row=0, column=0, sticky='nw')

# Add the header text to the canvas
header_text = "SMC Ticket Matrix"
canvas.create_text(110, 25, text=header_text, fill='green')
category_label = ttk.Label(text="Select Category:")
category_label.grid(row=1, column=0)
category_var = tk.StringVar()
# Call update_listbox when selection changes
category_var.trace_add('write', update_listbox)
category_dropdown = ttk.Combobox(textvariable=category_var, width=25)
category_dropdown.grid(row=1, column=1, sticky='new')


var = StringVar()
listbox1 = Listbox(root, listvariable=var)
listbox1.grid(row=1, column=0, sticky='new')

# Create the labels for the selection
catset = Label(root, text="Selection").grid(row=4, column=0, sticky="w")
prim = Label(root, text="Primary").grid(
    row=5, column=0, sticky="w")
sec = Label(root, text="Secondary").grid(row=6, column=0, sticky="w")
tri = Label(root, text="Tertiary").grid(row=7, column=0, sticky="w")

catset2 = Label(root, text="")
catset2.grid(row=4, column=1, sticky="w")
prim2 = Label(root, text="")
prim2.grid(row=5, column=1, sticky="w")
sec2 = Label(root, text="")
sec2.grid(row=6, column=1, sticky="w")
tri2 = Label(root, text="")
tri2.grid(row=7, column=1, sticky="w")
catset2.bind('<Button-1>')

# Bind the Listbox to update the labels when a new item is selected
listbox1.bind('<<ListboxSelect>>', update_listbox)


# Load initial category data
update_category_dropdown()
update_listbox()

root.title("SMC Ticket Matrix")
root.mainloop()
