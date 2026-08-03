'''GUI Calculator — Plan
Number buttons (0-9)
Operator buttons (+, -, *, /)
Equals (=) button 
Clear (C) button 
Display box'''
#----------------------------------------------------------
import tkinter as tk

window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x400")

display = tk.Entry(window, width=20, font=("Arial", 18), justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(value):
    display.insert(tk.END, value)

def clear_display():
    display.delete(0, tk.END)

def calculate():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(window, text=text, width=5, height=2, command=calculate)
    else:
        btn = tk.Button(window, text=text, width=5, height=2, 
                        command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

clear_btn = tk.Button(window, text="Clear", width=25, height=2, command=clear_display)
clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

window.mainloop()