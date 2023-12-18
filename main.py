import tkinter as tk
"""This program is a basic calculator that displays the whole calculator interface"""
def addition(x, y):
    """The addition function which takes the sum of two numbers and returns the value"""
    return x + y

def subtraction(x, y):
    """The subtraction function which takes the sum of two numbers and returns the value"""

    return x - y

def multiplication(x, y):
    """The multiplication function which takes the sum of two numbers and returns the value"""

    return x * y

def division(x, y):
    """The division function which divides two numbers and returns the value"""

    if y != 0:
        return x / y
    else:
        return "Error: not divisible by zero"

def run_calculator():
    """This function creates the main functionality of the program and uses tkinter as the GUI"""
    main = tk.Tk()
    main.title("Basic Calculator")
    main.geometry("1200x1000")

    input_frame = tk.Frame(main)
    input_frame.pack()

    input_num_1 = tk.Entry(input_frame, width=20)  # Adjust width to accommodate more characters
    input_operator = tk.Entry(input_frame, width=3)
    input_num_2 = tk.Entry(input_frame, width=20)  # Adjust width to accommodate more characters

    input_num_1.grid(row=0, column=0, padx=5, pady=5)
    input_operator.grid(row=0, column=1, padx=5, pady=5)
    input_num_2.grid(row=0, column=2, padx=5, pady=5)

    button_frame = tk.Frame(main)
    button_frame.pack()

    buttons = [
        '7', '8', '9',
        '4', '5', '6',
        '1', '2', '3',
        '0', '.', '+', '-',
        '*', '/', '='
    ]

    row_val = 1
    col_val = 0

    for button in buttons:
        tk.Button(button_frame, text=button, width=5, height=2, command=lambda b=button: on_button_click(b)).grid(row=row_val, column=col_val, padx=5, pady=5)
        col_val += 1
        if col_val > 2:
            col_val = 0
            row_val += 1

    outcome_var = tk.StringVar()
    outcome_label = tk.Label(main, textvariable=outcome_var)
    outcome_label.pack(pady=10)

    def on_button_click(button):
        current_text = input_num_1.get()

        if button in '0123456789.':
            input_num_1.insert(tk.END, button)
        elif button in '+-*/':
            input_operator.delete(0, tk.END)
            input_operator.insert(tk.END, button)
        elif button == '=':
            try:
                num1 = float(input_num_1.get())
                num2 = float(input_num_2.get())
                operator = input_operator.get()

                if operator == '+':
                    result = addition(num1, num2)
                elif operator == '-':
                    result = subtraction(num1, num2)
                elif operator == '*':
                    result = multiplication(num1, num2)
                elif operator == '/':
                    if num2 != 0:
                        result = division(num1, num2)
                    else:
                        result = "Error: Division by zero"

                outcome_var.set(result)
            except ValueError:
                outcome_var.set("Invalid input")

    main.mainloop()

if __name__ == "__main__":
    run_calculator()
