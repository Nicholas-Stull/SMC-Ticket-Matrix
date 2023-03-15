import tkinter as tk
import csv

def update_options(*args):
    selection = variable.get()
    secondary_menu['menu'].delete(0, 'end')
    tertiary_menu['menu'].delete(0, 'end')
    for i, row in enumerate(data):
        if row[0] == selection:
            secondary_list = row[1].split(',')
            tertiary_list = row[2].split(',')
            primary_list = row[3].split(',')
            break
    for choice in secondary_list:
        secondary_menu['menu'].add_command(label=choice, command=tk._setit(secondary_variable, choice))
    for choice in tertiary_list:
        tertiary_menu['menu'].add_command(label=choice, command=tk._setit(tertiary_variable, choice))
    primary_table.delete('all')
    primary_table.create_text(50, 20, text='Primary', font=('Arial', 14, 'bold'))
    for i, name in enumerate(primary_list):
        primary_table.create_text(50, 50+20*i, text=name, font=('Arial', 12))
    second_table.delete('all')
    second_table.create_text(50, 20, text='2nd', font=('Arial', 14, 'bold'))
    for i, name in enumerate(secondary_list):
        second_table.create_text(50, 50+20*i, text=name, font=('Arial', 12))
    third_table.delete('all')
    third_table.create_text(50, 20, text='3rd', font=('Arial', 14, 'bold'))
    for i, name in enumerate(tertiary_list):
        third_table.create_text(50, 50+20*i, text=name, font=('Arial', 12))

root = tk.Tk()
root.title('Dropdown Menu')

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

variable = tk.StringVar(root)
variable.set(data[0][0])

secondary_variable = tk.StringVar(root)

tertiary_variable = tk.StringVar(root)

variable.trace('w', update_options)

primary_table = tk.Canvas(root, width=200, height=120, bg='white')
primary_table.pack(side=tk.LEFT, padx=10)

second_table = tk.Canvas(root, width=200, height=120, bg='white')
second_table.pack(side=tk.LEFT, padx=10)

third_table = tk.Canvas(root, width=200, height=120, bg='white')
third_table.pack(side=tk.LEFT, padx=10)

secondary_menu = tk.OptionMenu(root, secondary_variable, '')
secondary_menu.pack(side=tk.LEFT, padx=10)

tertiary_menu = tk.OptionMenu(root, tertiary_variable, '')
tertiary_menu.pack(side=tk.LEFT, padx=10)

for row in data:
    variable_list = row[0]
    variable_menu = variable_list.split(',')
    variable_menu = [item.strip() for item in variable_menu]
    variable_list = tuple(variable_menu)
    variable.set(variable_list)
    break

for choice in variable_menu:
    variable_menu.remove(choice)
    variable_menu.insert(0, choice)
    secondary_menu['menu'].delete(0, 'end')
    tertiary_menu['menu'].delete(0, 'end')
    for item in variable_menu:
        secondary_menu['menu'].add_command(label=item, command=tk._setit(variable, item))

root.mainloop()
