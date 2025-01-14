"""Basiclly we creating a simple calcutor using tkinter to create user friendly interface
1.we are taking input numbers
2.we are checking whether the operation is valid or not
3.now we calculate the answer
4.we check whether the answer is in integer format or not ,
     If answer is equavalent to its integer format then display as integer.
     else not in integer format then display as it is.
5.after result is shown we can reset the values and calculate answer again and again
6.at last if user wants to exit then we can click exit button."""


import tkinter as tk
from tkinter import messagebox

def display(result):
    if result != int(result):
        result_label.config(text=f"The result is: {result}")
    else:
        result_label.config(text=f"The result is: {int(result)}")

def check_opr(operator):
    list_operators = ['+', '-', '/', '*']
    return operator in list_operators

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation and check_opr(operation):
            match operation:
                case '+':
                    display(num1 + num2)
                case '-':
                    display(num1 - num2)
                case '*':
                    display(num1 * num2)
                case '/':
                    if num2 != 0:
                        display(num1 / num2)
                    else:
                        messagebox.showerror("Error", "Division by zero is not allowed.")
        else:
            messagebox.showerror("Error", "Please select a valid operation.")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def reset_inputs():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    operation_var.set("")
    result_label.config(text="Result will be shown here.")

def exit_program():
    root.destroy()

# Tkinter UI setup
root = tk.Tk()
root.title("Simple Calculator")

# Number inputs
tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=10)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

# Operation selection
tk.Label(root, text="Select operation:").grid(row=2, column=0, padx=10, pady=10)
operation_var = tk.StringVar(value="")
tk.OptionMenu(root, operation_var, "+", "-", "*", "/").grid(row=2, column=1, padx=10, pady=10)

# Buttons for actions
tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, pady=10)
tk.Button(root, text="Reset", command=reset_inputs).grid(row=3, column=1, pady=10)
tk.Button(root, text="Exit", command=exit_program).grid(row=4, column=0, columnspan=2, pady=10)

# Result display
result_label = tk.Label(root, text="Result will be shown here.", fg="blue")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
