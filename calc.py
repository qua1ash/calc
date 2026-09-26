from tkinter import *
from tkinter import messagebox
import math


def add_number(number):
    global new_number
    if new_number:
        display_var.set("")
        new_number = False
    display_var.set(display_var.get() + number)


def choose_operation(action):
    global first_number, operation, new_number
    try:
        first_number = float(display_var.get())
        operation = action
        display_var.set(display_var.get() + " " + action + " ")
        new_number = False
    except ValueError:
        messagebox.showerror("Ошибка", "Сначала введите число")


def get_second_number():
    # После знака операции в поле остаётся второе число.
    return float(display_var.get().split()[-1])


def calculate():
    global operation, new_number
    try:
        second_number = get_second_number()

        if operation == "+":
            result = first_number + second_number
        elif operation == "-":
            result = first_number - second_number
        elif operation == "*":
            result = first_number * second_number
        elif operation == "/":
            result = first_number / second_number
        else:
            return

        display_var.set(str(result))
        operation = ""
        new_number = True
    except ZeroDivisionError:
        messagebox.showerror("Ошибка", "На ноль делить нельзя")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите второе число")


def square_root():
    global new_number
    try:
        number = float(display_var.get())
        display_var.set(str(math.sqrt(number)))
        new_number = True
    except ValueError:
        messagebox.showerror("Ошибка", "Введите число больше или равное нулю")


def clear():
    global first_number, operation, new_number
    first_number = 0
    operation = ""
    new_number = False
    display_var.set("")


window = Tk()
window.title("Калькулятор")
window.resizable(False, False)

first_number = 0
operation = ""
new_number = False
display_var = StringVar()

display = Entry(window, textvariable=display_var, font=("Arial", 18),
                justify="right", state="readonly", width=18)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("√", 4, 2), ("+", 4, 3),
]

for text, row, column in buttons:
    if text.isdigit():
        command = lambda value=text: add_number(value)
    elif text in "+-*/":
        command = lambda value=text: choose_operation(value)
    elif text == "√":
        command = square_root
    else:
        command = clear
    Button(window, text=text, width=5, height=2, command=command).grid(
        row=row, column=column, padx=2, pady=2)

Button(window, text="=", width=23, height=2, command=calculate).grid(
    row=5, column=0, columnspan=4, padx=2, pady=5)

window.mainloop()
