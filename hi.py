"""Simple calculator GUI."""

import tkinter as tk
from tkinter import messagebox


def calculate(operation):
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")
        return

    if operation == "Divide" and b == 0:
        messagebox.showerror("Math error", "Cannot divide by zero.")
        return

    result = {
        "Add": a + b,
        "Subtract": a - b,
        "Multiply": a * b,
        "Divide": a / b,
    }[operation]

    label_result.config(text=f"Result: {result}")


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("320x180")
root.resizable(False, False)

label_a = tk.Label(root, text="First number:")
label_a.grid(row=0, column=0, padx=10, pady=8, sticky="w")
entry_a = tk.Entry(root, width=20)
entry_a.grid(row=0, column=1, padx=10, pady=8)

label_b = tk.Label(root, text="Second number:")
label_b.grid(row=1, column=0, padx=10, pady=8, sticky="w")
entry_b = tk.Entry(root, width=20)
entry_b.grid(row=1, column=1, padx=10, pady=8)

button_frame = tk.Frame(root)
button_frame.grid(row=2, column=0, columnspan=2, pady=10)

for idx, op_name in enumerate(["Add", "Subtract", "Multiply", "Divide"]):
    button = tk.Button(button_frame, text=op_name, width=8, command=lambda name=op_name: calculate(name))
    button.grid(row=0, column=idx, padx=4)

label_result = tk.Label(root, text="Result:", font=(None, 12, "bold"))
label_result.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
