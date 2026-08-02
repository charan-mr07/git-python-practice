# 1. Layout Managers — 3 ways
label1.pack()
label2.pack()

# grid() — row, column
label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)
label2.grid(row=1, column=0)
entry2.grid(row=1, column=1)

# place() — exact x, y coordinates
label1.place(x=50, y=50)

# 2. More Widgets
# Checkbutton (checkbox)
var = tk.IntVar()
check = tk.Checkbutton(window, text="I agree", variable=var)
check.pack()

# Radiobutton
choice = tk.StringVar()
tk.Radiobutton(window, text="Male", variable=choice, value="Male").pack()
tk.Radiobutton(window, text="Female", variable=choice, value="Female").pack()

#Listbox (list of items, select)
listbox = tk.Listbox(window)
listbox.insert(1, "Physics")
listbox.insert(2, "Chemistry")
listbox.insert(3, "Maths")
listbox.pack()

#Messagebox (popup alerts)
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Info", "This is a message box!")

button = tk.Button(window, text="Show Message", command=show_message)
button.pack()

# 3. Full Example — Student Form
import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    course = course_var.get()
    messagebox.showinfo("Submitted", f"Name: {name}\nCourse: {course}")

window = tk.Tk()
window.title("Student Form")
window.geometry("300x250")

tk.Label(window, text="Name:").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1)

tk.Label(window, text="Course:").grid(row=1, column=0, padx=10, pady=10)
course_var = tk.StringVar()
tk.Radiobutton(window, text="ECE", variable=course_var, value="ECE").grid(row=1, column=1, sticky="w")
tk.Radiobutton(window, text="CSE", variable=course_var, value="CSE").grid(row=2, column=1, sticky="w")

submit_button = tk.Button(window, text="Submit", command=submit_form)
submit_button.grid(row=3, column=0, columnspan=2, pady=20)

window.mainloop()
