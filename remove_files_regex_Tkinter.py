import os
import re
from tkinter import filedialog
from tkinter import *


def delete_files(folder_path, regex_pattern):
    for filename in os.listdir(folder_path):
        if re.search(regex_pattern, filename):
            file_path = os.path.join(folder_path, filename)
            os.remove(file_path)
            print(f"Deleted file: {filename}")


def browse_folder():
    folder_path = filedialog.askdirectory()
    folder_entry.delete(0, END)
    folder_entry.insert(0, folder_path)


def delete_button_clicked():
    folder_path = folder_entry.get()
    regex_pattern = regex_entry.get()
    delete_files(folder_path, regex_pattern)
    messagebox.showinfo("Deletion Complete", "Files matching the pattern have been deleted.")


root = Tk()
root.title("File Deletion")
root.geometry("400x150")

folder_label = Label(root, text="Folder Path:")
folder_label.pack()

folder_entry = Entry(root, width=50)
folder_entry.pack()

browse_button = Button(root, text="Browse", command=browse_folder)
browse_button.pack()

regex_label = Label(root, text="Regex Pattern:")
regex_label.pack()

regex_entry = Entry(root, width=50)
regex_entry.pack()

delete_button = Button(root, text="Delete Files", command=delete_button_clicked)
delete_button.pack()

root.mainloop()
