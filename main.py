from tkinter import *


def plus():
    total_result = round(float(first_input) + float(second_input), 14)
    total_result = check_result(str(total_result))
    value.set(f"{total_result}")


def minus():
    total_result = round(float(first_input) - float(second_input), 14)
    total_result = check_result(str(total_result))
    value.set(f"{total_result}")


def multiply():
    total_result = round(float(first_input) * float(second_input), 14)
    total_result = check_result(str(total_result))
    value.set(f"{total_result}")


def divide():
    total_result = round(float(first_input) / float(second_input), 14)
    total_result = check_result(str(total_result))
    value.set(f"{total_result}")


def fraction():
    total_result = round(1 / int(first_input), 14)
    total_result = check_result(str(total_result))
    value.set(f"{total_result}")


def percent():
    if operation == "+":
        total_result = round(float(first_input) + (float(first_input) * (float(second_input) / 100)), 14)
        total_result = check_result(str(total_result))
        value.set(f"{total_result}")
    elif operation == "-":
        total_result = round(float(first_input) - (float(first_input) * (float(second_input) / 100)), 14)
        total_result = check_result(str(total_result))
        value.set(f"{total_result}")


def check_result(rs):
    all_parts = rs.split(".")
    first_part = all_parts[0]
    second_parts = all_parts[1]

    if len(second_parts) == 1 and second_parts == "0":
        return first_part
    else:
        return rs


def remove_last_symbol(text):
    new_input = ""

    ind = len(text) - 1
    new_input += text[:ind]

    if new_input == "":
        new_input = "0"

    return new_input


def add_remove_prefix():
    global first_input
    global second_input
    global next_input
    new_text = ""

    if next_input:
        text = second_input
    else:
        text = first_input

    if text.startswith("-"):
        new_text += text[1:]
    else:
        new_text += '-'
        new_text += text

    if next_input:
        second_input = new_text
        value.set(second_input)
    else:
        first_input = new_text
        value.set(first_input)


def bind_comma():
    global first_input
    global second_input
    f_has = False
    s_has = False

    for i in first_input:
        if i == ".":
            f_has = True

    for i in second_input:
        if i == ".":
            s_has = True

    if len(first_input) > 0 and not f_has:
        first_input += "."
        value.set(first_input)

    elif len(second_input) > 0 and not s_has:
        second_input += "."
        value.set(second_input)


def del_last_symbol():
    global first_input
    global second_input
    global next_input

    if next_input:
        second_input = remove_last_symbol(second_input)
        value.set(second_input)
    else:
        first_input = remove_last_symbol(first_input)
        value.set(first_input)


def joining(in_put):
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


def clean():
    global first_input
    global second_input
    global operation
    global next_input

    first_input = ""
    second_input = ""
    operation = ""
    next_input = False

    value.set("0")


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


def memory_clean():
    global memory_mc

    memory_mc = ""


def memory_read():
    pass


def memory_save():
    pass


def memory_plus():
    pass


def memory_minus():
    pass


window = Tk()
window.title("CALCULATOR")
window.geometry("400x550")
window.resizable(False, False)
window.config(bg="#33415c", pady=16, padx=18)

first_input = ""
second_input = ""
operation = ""
next_input = False
memory_mc = ""

value = StringVar()
value.set("0")

label = Label(window, textvariable=value)
label.config(bg="#33415c", width=24, height=2, font="helvetica 30", anchor="e", foreground="#fff")
label.pack()

frame = Frame(window)
frame.config(bg="#33415c")
frame.pack()

# first row(0) - memory buttons

button_MC = Button(frame, text="MC", command=lambda: memory_clean())
button_MC.config(width=5, height=2, font="helvetica 16", fg="#33415c", relief="groove")
button_MC.grid(column=0, row=0)

button_MR = Button(frame, text="MR", command=lambda: memory_read())
button_MR.config(width=5, height=2, font="helvetica 16", fg="#33415c", relief="groove")
button_MR.grid(column=1, row=0)

button_MS = Button(frame, text="MS", command=lambda: memory_save())
button_MS.config(width=5, height=2, font="helvetica 16", fg="#33415c", relief="groove")
button_MS.grid(column=2, row=0)

button_Mplus = Button(frame, text="M+", command=lambda: memory_plus())
button_Mplus.config(width=5, height=2, font="helvetica 16", fg="#33415c", relief="groove")
button_Mplus.grid(column=3, row=0)

button_Mminus = Button(frame, text="M-", command=lambda: memory_minus())
button_Mminus.config(width=5, height=2, font="helvetica 16", fg="#33415c", relief="groove")
button_Mminus.grid(column=4, row=0)

# second row(1) - clean/delete last int buttons

button_clean = Button(frame, text="C", command=clean)
button_clean.config(width=11, height=2, font="helvetica 14 bold", fg="#33415c", relief="groove")
button_clean.grid(column=0, columnspan=2, row=1)

button_del = Button(frame, text="<--", command=del_last_symbol)
button_del.config(width=11, height=2, font="helvetica 14 bold", fg="#33415c", relief="groove")
button_del.grid(column=2, columnspan=2, row=1)

button_positive_negative = Button(frame, text="+/-", command=add_remove_prefix)
button_positive_negative.config(width=5, height=2, font="helvetica 14 bold", fg="#33415c", relief="groove")
button_positive_negative.grid(column=4, row=1)

# int buttons

button_1 = Button(frame, text="1", command=lambda: joining(1))
button_1.config(width=5, height=2, font=40, relief="groove")
button_1.grid(column=0, row=4)

button_2 = Button(frame, text="2", command=lambda: joining(2))
button_2.config(width=5, height=2, font=40, relief="groove")
button_2.grid(column=1, row=4)

button_3 = Button(frame, text="3", command=lambda: joining(3))
button_3.config(width=5, height=2, font=40, relief="groove")
button_3.grid(column=2, row=4)

button_4 = Button(frame, text="4", command=lambda: joining(4))
button_4.config(width=5, height=2, font=40, relief="groove")
button_4.grid(column=0, row=3)

button_5 = Button(frame, text="5", command=lambda: joining(5))
button_5.config(width=5, height=2, font=40, relief="groove")
button_5.grid(column=1, row=3)

button_6 = Button(frame, text="6", command=lambda: joining(6))
button_6.config(width=5, height=2, font=40, relief="groove")
button_6.grid(column=2, row=3)

button_7 = Button(frame, text="7", command=lambda: joining(7))
button_7.config(width=5, height=2, font=40, relief="groove")
button_7.grid(column=0, row=2)

button_8 = Button(frame, text="8", command=lambda: joining(8))
button_8.config(width=5, height=2, font=40, relief="groove")
button_8.grid(column=1, row=2)

button_9 = Button(frame, text="9", command=lambda: joining(9))
button_9.config(width=5, height=2, font=40, relief="groove")
button_9.grid(column=2, row=2)

button_0 = Button(frame, text="0", command=lambda: joining(0))
button_0.config(width=11, height=2, font=40, relief="groove")
button_0.grid(column=0, columnspan=2, row=5)

button_comma = Button(frame, text=".", command=lambda: bind_comma())
button_comma.config(width=5, height=2, font=40, relief="groove")
button_comma.grid(column=2, row=5)

# operation buttons

button_plus = Button(frame, text="+", command=lambda: joining("+"))
button_plus.config(width=5, height=2, font=40, borderwidth=2, relief="groove")
button_plus.grid(column=3, row=4)

button_minus = Button(frame, text="-", command=lambda: joining("-"))
button_minus.config(width=5, height=2, font=40, borderwidth=2, relief="groove")
button_minus.grid(column=4, row=4)

button_multiple = Button(frame, text="x", command=lambda: joining("*"))
button_multiple.config(width=5, height=2, font=40, borderwidth=2, relief="groove")
button_multiple.grid(column=3, row=3)

button_divide = Button(frame, text="/", command=lambda: joining("/"))
button_divide.config(width=5, height=2, font=40, borderwidth=2, relief="groove")
button_divide.grid(column=4, row=3)

button_fraction = Button(frame, text="1/a", command=fraction)
button_fraction.config(width=5, height=2, font=40, borderwidth=2, relief="groove")
button_fraction.grid(column=3, row=2)

button_percent = Button(frame, text="%", command=percent)
button_percent.config(width=5, height=2, font=40, borderwidth=2, relief="groove")
button_percent.grid(column=4, row=2)

button_result = Button(frame, text="=", command=result)
button_result.config(width=11, height=2, font=40, bg="#f3dfa2", relief="groove")
button_result.grid(column=3, columnspan=2, row=5)

window.mainloop()
