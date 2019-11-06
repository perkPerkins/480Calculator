from tkinter import *
import Calculator

root = Tk()
root.title("480 Calculator")
calc = Calculator.Calculator()

calculation_entry = Entry(root, width=25, borderwidth=5)

calculation_entry.grid(row=0, column=0,  columnspan=4, padx=10, pady=10)


def button_click(operand_or_operator):
    current = calculation_entry.get()
    calculation_entry.delete(0, END)
    calculation_entry.insert(0, current + operand_or_operator)
    return


def clear_entry_box():
    calculation_entry.delete(0, END)


def equals_button():
    expression = calculation_entry.get()
    value = calc.API(str(expression))
    calculation_entry.delete(0, END)
    if value == "Invalid Expression":
        calculation_entry.delete(0, END)
        calculation_entry.insert(0, value)
    else:
        calculation_entry.insert(0, value)

# Define buttons


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click("1"))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click("2"))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click("3"))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click("4"))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click("5"))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click("6"))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click("7"))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click("8"))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click("9"))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click("0"))
button_plus = Button(root, text="+", padx=40, pady=20, command=lambda: button_click("+"))
button_minus = Button(root, text="-", padx=40, pady=20, command=lambda: button_click("-"))
button_mult = Button(root, text="*", padx=40, pady=20, command=lambda: button_click("*"))
button_div = Button(root, text="/", padx=40, pady=20, command=lambda: button_click("/"))
button_exponent = Button(root, text="^", padx=40, pady=20, command=lambda: button_click("^"))
button_equal = Button(root, text="=", padx=40, pady=20, command=equals_button)
button_clear = Button(root, text="AC", padx=35, pady=20, command=clear_entry_box)
button_negative = Button(root, text="Negative", padx=15, pady=20, command=lambda: button_click("n"))
button_left_parenth = Button(root, text="(", padx=40, pady=20, command=lambda: button_click("("))
button_right_parenth = Button(root, text=")", padx=40, pady=20, command=lambda: button_click(")"))

# Put buttons on screen

button_clear.grid(row=1, column=0)
button_left_parenth.grid(row=1, column=1)
button_right_parenth.grid(row=1, column=2)
button_div.grid(row=1, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_mult.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_minus.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_plus.grid(row=4, column=3)

button_0.grid(row=5, column=0)
button_equal.grid(row=5, column=1)
button_exponent.grid(row=5, column=2)
button_negative.grid(row=5, column=3)

root.mainloop()
