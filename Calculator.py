import tkinter as tk
from tkinter import messagebox
import math

def evaluate_expression(expression):
    try:
        return str(eval(expression))  # Using eval to handle operator precedence correctly
    except Exception as e:
        return "Error"

def on_click(button_text):
    if button_text == "=":
        try:
            result = evaluate_expression(entry_var.get())
            history_listbox.insert(0, entry_var.get() + " = " + result)  # Insert at the top
            entry_var.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            entry_var.set("")
    elif button_text == "C":
        entry_var.set("")  # Clear the entry
    elif button_text == "⌫":  # Backspace functionality
        entry_var.set(entry_var.get()[:-1])
    elif button_text in ["sin", "cos", "tan", "log", "sqrt"]:
        try:
            expr = entry_var.get()
            if button_text == "sin":
                result = str(math.sin(math.radians(float(expr))))
            elif button_text == "cos":
                result = str(math.cos(math.radians(float(expr))))
            elif button_text == "tan":
                result = str(math.tan(math.radians(float(expr))))
            elif button_text == "log":
                result = str(math.log10(float(expr)))
            elif button_text == "sqrt":
                result = str(math.sqrt(float(expr)))
            history_listbox.insert(0, button_text + "(" + expr + ") = " + result)  # Insert at the top
            entry_var.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input for Function")
            entry_var.set("")
    else:
        entry_var.set(entry_var.get() + button_text)  # Append the button text to the entry

def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        root.configure(bg="#2E2E2E")  # Dark mode background
        entry.configure(bg="#555", fg="white")
        history_listbox.configure(bg="#333", fg="white")
        for btn in buttons_list:
            btn.configure(bg="#444", fg="white", activebackground="#666")
    else:
        root.configure(bg="#A67B5B")  # Light mode background
        entry.configure(bg="#D2B48C", fg="black")
        history_listbox.configure(bg="#FFF8DC", fg="black")
        for btn in buttons_list:
            btn.configure(bg="#8B5A2B", fg="white", activebackground="#A0522D")

def on_key(event):
    key = event.char
    if key in "0123456789+-*/.=":
        on_click(key)
    elif key == "\r":  # Enter key
        on_click("=")
    elif key == "\x08":  # Backspace key
        on_click("⌫")

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")  # Adjusted size to fit the window better
root.configure(bg="#A67B5B")  # Aesthetic brown background
root.resizable(False, False)  # Prevent resizing

dark_mode = False

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 16), justify='right', bg="#D2B48C", fg="black")
entry.grid(row=0, column=0, columnspan=4, ipadx=5, ipady=5, pady=5, sticky="nsew")
root.bind("<Key>", on_key)  # Bind key events to the entry

# History display
history_listbox = tk.Listbox(root, font=("Arial", 12), height=2, bg="#FFF8DC", fg="black")  # Reduced height
history_listbox.grid(row=1, column=0, columnspan=4, pady=5, padx=5, sticky="nsew")

buttons = [
    ('C', '⌫', 'log', 'sqrt'),
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+'),
    ('sin', 'cos', 'tan', 'Dark\nMode')
]

button_bg = "#8B5A2B"  # Dark brown
button_fg = "white"  # White text
button_active_bg = "#A0522D"  # Lighter brown on click

buttons_list = []
for r, row in enumerate(buttons, start=2):
    for c, btn_text in enumerate(row):
        btn = tk.Button(root, text=btn_text, font=("Arial", 14), width=6, height=2,  # Adjusted font size
                         bg=button_bg, fg=button_fg, activebackground=button_active_bg,
                         command=lambda t=btn_text: toggle_dark_mode() if t == "Dark\nMode" else on_click(t))
        btn.grid(row=r, column=c, padx=3, pady=3, sticky="nsew")
        buttons_list.append(btn)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)  # Make columns expand equally
for i in range(2, len(buttons) + 2):
    root.grid_rowconfigure(i, weight=1)  # Make rows expand equally

root.mainloop()  # Start the main event loop
