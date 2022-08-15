# https://github.com/alien-max
from tkinter import *

################################################################# main window
calculator = Tk()
calculator.title("calculator")
calculator.resizable(width=False,height=False)

################################################################# vars
text_input = StringVar()
expression = ""
operator = ""

################################################################# functions
def set_number(number):
    global expression
    expression = expression + str(number)
    text_input.set(expression)

def set_operator(op):
    global operator
    global expression
    operator = op
    expression = expression + str(operator)
    text_input.set(expression)

def show_result():
    global expression
    result = str(eval(expression)) 
    text_input.set(result)
    expression = ""

def clear_num():
    global expression
    expression = ""
    text_input.set("")

################################################################# label
txt_display = Entry(calculator, font=('time new roman', 22, 'bold'),
 textvariable=text_input, bd=30, insertwidth=5, bg='powder blue',
 justify='right',).grid(columnspan=4)

################################################################# buttons
btn7 = Button(calculator, padx=12, pady=10, bd=20, fg='gray', font=('time new roman', 22, 'bold'),
 text='7',command=lambda:set_number(7)).grid(row=1, column=0)
btn8 = Button(calculator, padx=12, pady=10, bd=20, fg='gray', font=('time new roman', 22, 'bold'),
 text='8',command=lambda:set_number(8)).grid(row=1, column=1)
btn9 = Button(calculator, padx=12, pady=10, bd=20, fg='gray', font=('time new roman', 22, 'bold'),
 text='9',command=lambda:set_number(9)).grid(row=1, column=2)
btnsub = Button(calculator, padx=12, pady=10, bd=20, fg='gray', font=('time new roman', 22, 'bold'),
 text='-',command=lambda:set_operator('-')).grid(row=1, column=3)


btn4 = Button(calculator, padx=12, pady=10, bd=20, fg='gray', font=('time new roman', 22, 'bold'),
 text='4',command=lambda:set_number(4)).grid(row=2, column=0)
btn5 = Button(calculator, padx=12, pady=10, bd=20, fg='gray', font=('time new roman', 22, 'bold'),
 text='5',command=lambda:set_number(5)).grid(row=2, column=1)
btn6 = Button(calculator, padx=12, pady=10, bd=20, fg='gray', font=('time new roman', 22, 'bold'),
 text='6',command=lambda:set_number(6)).grid(row=2, column=2)
btnplus = Button(calculator, padx=12, pady=10, bd=20, fg='gray', font=('time new roman', 22, 'bold'),
 text='+',command=lambda:set_operator('+')).grid(row=2, column=3)


btn1 = Button(calculator, padx=12, pady=10, bd=20, fg='gray', font=('time new roman', 22, 'bold'),
 text='1',command=lambda:set_number(1)).grid(row=3, column=0)
btn2 = Button(calculator, padx=12, pady=10, bd=20, fg='gray', font=('time new roman', 22, 'bold'),
 text='2',command=lambda:set_number(2)).grid(row=3, column=1)
btn3 = Button(calculator, padx=12, pady=10, bd=20, fg='gray', font=('time new roman', 22, 'bold'),
 text='3',command=lambda:set_number(3)).grid(row=3, column=2)
btnmulti = Button(calculator, padx=12, pady=10, bd=20, fg='gray', font=('time new roman', 22, 'bold'),
 text='*',command=lambda:set_operator('*')).grid(row=3, column=3)


btn0 = Button(calculator, padx=12, pady=10, bd=20, fg='gray', font=('time new roman', 22, 'bold'),
 text='0',command=lambda:set_number(0)).grid(row=4, column=0)
btnc = Button(calculator, padx=12, pady=10, bd=20, fg='gray', font=('time new roman', 22, 'bold'),
 text='C',command=lambda:clear_num()).grid(row=4, column=1)
btnequ = Button(calculator, padx=12, pady=10, bd=20, fg='gray', font=('time new roman', 22, 'bold'),
 text='=',command=lambda:show_result()).grid(row=4, column=2)
btndivi = Button(calculator, padx=12, pady=10, bd=20, fg='gray', font=('time new roman', 22, 'bold'),
 text='/',command=lambda:set_operator('/')).grid(row=4, column=3)

calculator.mainloop()
