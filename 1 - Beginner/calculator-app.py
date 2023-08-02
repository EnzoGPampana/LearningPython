# Calculator
# Tier: 1-Beginner
# Calculators are not only one of the most useful tools available, but they are also a great way to understand UI and event processing in an application. 
# In this problem you will create a calculator that supports basic arithmetic calculations on integers.
# The styling is up to you so use your imagination and get creative! 
# You might also find it worth your time to experiment with the calculator app on your mobile device to better understand basic functionality and edge cases.

from tkinter import *

def button_press(num):
    global equation_text

    equation_text = equation_text + str(num)
    equationn_label.set(equation_text)

def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equationn_label.set(total)

        equation_text = total
    except ZeroDivisionError:
        equationn_label.set("ERROR! Division by zero !!")
        equation_text = "" 
    except SyntaxError:
            equationn_label.set("ERROR! Syntax error !!")

def clear():
        global equation_text

        equationn_label.set("")

        equation_text = ""


window = Tk()
window.title("Calculator - APP")
window.geometry("500x500")

equation_text = ""
equationn_label = StringVar()

label =Label(window, textvariable=equationn_label, font='consolas', bg="white", width=40, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4,width=9, font=35, command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4,width=9, font=35, command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4,width=9, font=35, command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4,width=9, font=35, command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4,width=9, font=35, command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4,width=9, font=35, command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4,width=9, font=35, command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4,width=9, font=35, command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4,width=9, font=35, command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4,width=9, font=35, command=lambda: button_press(0))
button0.grid(row=3, column=0)

plus = Button(frame, text='+', height=4,width=9, font=35, command=lambda: button_press('+'))
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=4,width=9, font=35, command=lambda: button_press('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, text='X', height=4,width=9, font=35, command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text='/', height=4,width=9, font=35, command=lambda: button_press('/'))
divide.grid(row=3, column=3)

decimal = Button(frame, text='.', height=4,width=9, font=35, command=lambda: button_press('.'))
decimal.grid(row=3, column=1)

equal = Button(frame, text='=', height=4,width=9, font=35, command=equals)
equal.grid(row=3, column=2)

clear = Button(window, text='Clear', height=4,width=25, font=35, command=clear)
clear.pack()
window.mainloop()