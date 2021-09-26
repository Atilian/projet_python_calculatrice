#!/usr/bin/python3
from tkinter import *

window = Tk()

window.title("Calculatrice")

window.minsize(480,500)

window.maxsize(480,500)

display = Entry(window)
display.place(width=435, height=100, x=20, y=15)

button_width = 80
button_height = 70

def button_display(value):
    if (value == "E"):
        answer = eval(display.get())
        display.delete(0, "end")
        display.insert(0, answer)
    elif (value == "R"):
        display.delete(0, "end")
    else:    
        display.insert("end", value)

# ********************************************** #
#Column 1

number_reset = Button(window, text="R", command=lambda: button_display(("R")))
number_reset.place(width=button_width, height=button_height, x=20, y=135)

number_div = Button(window, text="/", command=lambda: button_display(("/")))
number_div.place(width=button_width, height=button_height, x=110, y=135)

number_mult = Button(window, text="*", command=lambda: button_display(("*")))
number_mult.place(width=button_width, height=button_height, x=200, y=135)

number_sous = Button(window, text="-", command=lambda: button_display(("-")))
number_sous.place(width=button_width, height=button_height, x=290, y=135)

# ********************************************** #
#Column 1

number_7 = Button(window, text="7", command=lambda: button_display("7"))
number_7.place(width=button_width, height=button_height, x=20, y=205)

number_8 = Button(window, text="8", command=lambda: button_display(("8")))
number_8.place(width=button_width, height=button_height, x=110, y=205)

number_9 = Button(window, text="9", command=lambda: button_display(("9")))
number_9.place(width=button_width, height=button_height, x=200, y=205)

number_add = Button(window, text="+", command=lambda: button_display(("+")))
number_add.place(width=button_width, height=138, x=290, y=205)

# ********************************************** #
#Column 2

number_4 = Button(window, text="4", command=lambda: button_display(("4")))
number_4.place(width=button_width, height=button_height, x=20, y=275)

number_5 = Button(window, text="5", command=lambda: button_display(("5")))
number_5.place(width=button_width, height=button_height, x=110, y=275)

number_6 = Button(window, text="6", command=lambda: button_display(("6")))
number_6.place(width=button_width, height=button_height, x=200, y=275)

# ********************************************** #
#Column 3

number_1 = Button(window, text="1", command=lambda: button_display(("1")))
number_1.place(width=button_width, height=button_height, x=20, y=345)

number_2 = Button(window, text="2", command=lambda: button_display(("2")))
number_2.place(width=button_width, height=button_height, x=110, y=345)

number_3 = Button(window, text="3", command=lambda: button_display(("3")))
number_3.place(width=button_width, height=button_height, x=200, y=345)

number_ent = Button(window, text="E", command=lambda: button_display(("E")))
number_ent.place(width=button_width, height=138, x=290, y=345)

# ********************************************** #
#Column 3

number_0 = Button(window, text="0", command=lambda: button_display(("0")))
number_0.place(width=170, height=button_height, x=20, y=415)

number_dot = Button(window, text=".", command=lambda: button_display((".")))
number_dot.place(width=button_width, height=button_height, x=200, y=415)






window.mainloop()