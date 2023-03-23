import tkinter as tk
import csv


class App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x400")  # set window size
        self.master.title("CSV Search")

        # create search bar
        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.update_list)
        self.search_entry = tk.Entry(self.master, textvariable=self.search_var)
        self.search_entry.pack()

        # create listbox
        self.listbox = tk.Listbox(
            self.master, width=80, height=20)  # set listbox size
        self.listbox.pack()
        self.listbox.bind("<<ListboxSelect>>", self.display_labels)

        # create labels for primary, secondary, and tertiary columns
        self.primary_label = tk.Label(self.master, text="")
        self.primary_label.pack()
        self.secondary_label = tk.Label(self.master, text="")
        self.secondary_label.pack()
        self.tertiary_label = tk.Label(self.master, text="")
        self.tertiary_label.pack()

        # read data from CSV file
        self.data = []
        with open('src/csv/MatrixFull.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                self.data.append(row)

        # display all data in listbox
        self.update_list()

    def update_list(self, *args):
        search_term = self.search_var.get().lower()
        self.listbox.delete(0, tk.END)

        # loop through data and add matches to listbox
        for row in self.data:
            if search_term in row[0].lower():
                self.listbox.insert(tk.END, row[0])

        # select first item in listbox
        self.listbox.selection_clear(0, tk.END)
        if self.listbox.size() > 0:
            self.listbox.selection_set(0)
            self.display_labels(None)

    def display_labels(self, event):
        # get selected item from listbox
        if self.listbox.curselection():
            index = self.listbox.curselection()[0]
            selected_item = self.listbox.get(index)

            # loop through data and find matching row
            for row in self.data:
                if selected_item == row[0]:
                    self.primary_label.config(text="Primary: " + row[1])
                    self.secondary_label.config(text="Secondary: " + row[2])
                    self.tertiary_label.config(text="Tertiary: " + row[3])
                    break


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
