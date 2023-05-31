from tkinter import *


def plus():
    total_result = str(int(first_input) + int(second_input))
    value.set(total_result)


def minus():
    total_result = str(int(first_input) - int(second_input))
    value.set(total_result)


def multiply():
    total_result = str(int(first_input) * int(second_input))
    value.set(total_result)


def divide():
    total_result = str(int(first_input) / int(second_input))
    value.set(total_result)


def calculation(in_put):
    global first_input
    global second_input
    global operation
    global next_input

    if not str(in_put).isdigit():
        operation = in_put
        next_input = True
        value.set(in_put)
    elif not next_input:
        first_input = first_input + str(in_put)
        value.set(first_input)
    else:
        second_input = second_input + str(in_put)
        value.set(second_input)


def clear():
    global first_input
    global second_input
    global operation
    global next_input

    first_input = ""
    second_input = ""
    operation = ""
    next_input = False

    value.set("")


def result():
    global operation

    if operation == "+":
        plus()
    elif operation == "-":
        minus()
    elif operation == "*":
        multiply()
    elif operation == "/":
        divide()


window = Tk()
window.title("CALCULATOR")
window.geometry("400x400")
window.config(bg="darkgray")

first_input = ""
second_input = ""
operation = ""
next_input = False

value = StringVar()

label = Label(window, textvariable=value, background="white", width=39, height=2)
label.pack()

frame = Frame(window, background="darkgray")
frame.pack()

button_1 = Button(frame, text="1", width=5, height=2, font=40, command=lambda: calculation(1))
button_1.grid(column=0, row=2)

button_2 = Button(frame, text="2", width=5, height=2, font=40, command=lambda: calculation(2))
button_2.grid(column=1, row=2)

button_3 = Button(frame, text="3", width=5, height=2, font=40, command=lambda: calculation(3))
button_3.grid(column=2, row=2)

button_4 = Button(frame, text="4", width=5, height=2, font=40, command=lambda: calculation(4))
button_4.grid(column=0, row=1)

button_5 = Button(frame, text="5", width=5, height=2, font=40, command=lambda: calculation(5))
button_5.grid(column=1, row=1)

button_6 = Button(frame, text="6", width=5, height=2, font=40, command=lambda: calculation(6))
button_6.grid(column=2, row=1)

button_7 = Button(frame, text="7", width=5, height=2, font=40, command=lambda: calculation(7))
button_7.grid(column=0, row=0)

button_8 = Button(frame, text="8", width=5, height=2, font=40, command=lambda: calculation(8))
button_8.grid(column=1, row=0)

button_9 = Button(frame, text="9", width=5, height=2, font=40, command=lambda: calculation(9))
button_9.grid(column=2, row=0)

button_0 = Button(frame, text="0", width=5, height=2, font=40, command=lambda: calculation(0))
button_0.grid(column=1, row=3)

button_clear = Button(frame, text="C", width=5, height=2, font=40, command=clear)
button_clear.grid(column=0, row=3)

button_plus = Button(frame, text="+", width=5, height=2, font=40, command=lambda: calculation("+"))
button_plus.grid(column=3, row=0)

button_minus = Button(frame, text="-", width=5, height=2, font=40, command=lambda: calculation("-"))
button_minus.grid(column=3, row=1)

button_multiple = Button(frame, text="*", width=5, height=2, font=40, command=lambda: calculation("*"))
button_multiple.grid(column=3, row=2)

button_divide = Button(frame, text="/", width=5, height=2, font=40, command=lambda: calculation("/"))
button_divide.grid(column=3, row=3)

button_result = Button(frame, text="=", width=5, height=2, font=40, command=result)
button_result.grid(column=2, row=3)

window.mainloop()
