# tkinter is a built-in GUI library that comes with Python itself
#1. Creating a Basic Window
import tkinter as tk

window = tk.Tk()           # creating the window object
window.title("My First GUI")
window.geometry("300x200")  # width x height

window.mainloop()           # keeps the window open (without this, it closes instantly)

#2. Adding a Label (to display text)
import tkinter as tk

window = tk.Tk()
window.title("My First GUI")
window.geometry("300x200")

label = tk.Label(window, text="Hello, Charan!")
label.pack()   # places the widget inside the window

window.mainloop()

#3. Adding a Button (to do something when clicked)
import tkinter as tk

def on_click():
    label.config(text="Button clicked!")

window = tk.Tk()
window.title("My First GUI")
window.geometry("300x200")

label = tk.Label(window, text="Hello, Charan!")
label.pack()

button = tk.Button(window, text="Click Me", command=on_click)
button.pack()

window.mainloop()

#4. Adding an Entry (text input box)
import tkinter as tk

def greet_user():
    name = entry.get()
    label.config(text="Hello, " + name + "!")

window = tk.Tk()
window.title("Greeting App")
window.geometry("300x200")

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Greet", command=greet_user)
button.pack()

label = tk.Label(window, text="")
label.pack()

window.mainloop()

