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
window.geometry("320x350")
window.config(bg="#33415c", pady=16, padx=21)

first_input = ""
second_input = ""
operation = ""
next_input = False

value = StringVar()

label = Label(window, textvariable=value)
label.config(bg="#33415c", width=24, height=2, font=40, anchor="e", foreground="#fff")
label.pack()

print(label.configure().keys())

frame = Frame(window)
frame.config(bg="#33415c")
frame.pack()

button_1 = Button(frame, text="1", command=lambda: calculation(1))
button_1.config(width=5, height=2, font=40, borderwidth=2, relief="groove")
button_1.grid(column=0, row=2)

button_2 = Button(frame, text="2", command=lambda: calculation(2))
button_2.config(width=5, height=2, font=40, borderwidth=2, relief="groove")
button_2.grid(column=1, row=2)

button_3 = Button(frame, text="3", command=lambda: calculation(3))
button_3.config(width=5, height=2, font=40, borderwidth=2, relief="groove")
button_3.grid(column=2, row=2)

button_4 = Button(frame, text="4", command=lambda: calculation(4))
button_4.config(width=5, height=2, font=40, borderwidth=2, relief="groove")
button_4.grid(column=0, row=1)

button_5 = Button(frame, text="5", command=lambda: calculation(5))
button_5.config(width=5, height=2, font=40, borderwidth=2, relief="groove")
button_5.grid(column=1, row=1)

button_6 = Button(frame, text="6", command=lambda: calculation(6))
button_6.config(width=5, height=2, font=40, borderwidth=2, relief="groove")
button_6.grid(column=2, row=1)

button_7 = Button(frame, text="7", command=lambda: calculation(7))
button_7.config(width=5, height=2, font=40, borderwidth=2, relief="groove")
button_7.grid(column=0, row=0)

button_8 = Button(frame, text="8", command=lambda: calculation(8))
button_8.config(width=5, height=2, font=40, borderwidth=2, relief="groove")
button_8.grid(column=1, row=0)

button_9 = Button(frame, text="9", command=lambda: calculation(9))
button_9.config(width=5, height=2, font=40, borderwidth=2, relief="groove")
button_9.grid(column=2, row=0)

button_0 = Button(frame, text="0", command=lambda: calculation(0))
button_0.config(width=5, height=2, font=40, borderwidth=2, relief="groove")
button_0.grid(column=1, row=3)

button_clear = Button(frame, text="C", command=clear)
button_clear.config(width=5, height=2, font=40, borderwidth=2, fg="#33415c", relief="groove")
button_clear.grid(column=0, row=3)

button_plus = Button(frame, text="+", command=lambda: calculation("+"))
button_plus.config(width=5, height=2, font=40, borderwidth=2, relief="groove")
button_plus.grid(column=3, row=0)

button_minus = Button(frame, text="-", command=lambda: calculation("-"))
button_minus.config(width=5, height=2, font=40, borderwidth=2, relief="groove")
button_minus.grid(column=3, row=1)

button_multiple = Button(frame, text="x", command=lambda: calculation("*"))
button_multiple.config(width=5, height=2, font=40, borderwidth=2, relief="groove")
button_multiple.grid(column=3, row=2)

button_divide = Button(frame, text="/", command=lambda: calculation("/"))
button_divide.config(width=5, height=2, font=40, borderwidth=2, relief="groove")
button_divide.grid(column=3, row=3)

button_result = Button(frame, text="=", command=result)
button_result.config(width=5, height=2, font=40, borderwidth=2, bg="#f3dfa2", relief="groove")
button_result.grid(column=2, row=3)

window.mainloop()
