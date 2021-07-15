from tkinter import *

window = Tk()
window.title("Calculadora")

i = 0 

# Text Entry
entry_text = Entry(window)
entry_text.grid(row = 0, column = 0, columnspan = 4, padx =5, pady =5)
 
 #functions
 
def button_op(value):
    global i
    entry_text.insert(i , value)
    i += 1 
 
def erase():
    entry_text.delete(0, END)
    i = 0 
 
def make_op():
    equation = entry_text.get()
    result = eval(equation)
    entry_text.delete(0, END)
    entry_text.insert(0, result)
 
 
#buttons
 
button1 = Button(window, text="1", width= 5, height= 2, command= lambda: button_op (1))
button2 = Button(window, text="2", width= 5, height= 2, command= lambda: button_op (2))
button3 = Button(window, text="3", width= 5, height= 2, command= lambda: button_op (3))
button4 = Button(window, text="4", width= 5, height= 2, command= lambda: button_op (4))
button5 = Button(window, text="5", width= 5, height= 2, command= lambda: button_op (5))
button6 = Button(window, text="6", width= 5, height= 2, command= lambda: button_op (6))
button7 = Button(window, text="7", width= 5, height= 2, command= lambda: button_op (7))
button8 = Button(window, text="8", width= 5, height= 2, command= lambda: button_op (8))
button9 = Button(window, text="9", width= 5, height= 2, command= lambda: button_op (9))
button0 = Button(window, text="0", width= 13, height= 2, command= lambda: button_op (0))
 
button_erase = Button(window, text="AC", width= 5, height= 2, command= lambda: erase ())
button_paren1 = Button(window, text="(", width= 5, height= 2, command= lambda: button_op ("("))
button_paren2 = Button(window, text=")", width= 5, height= 2, command= lambda: button_op (")"))
button_dot = Button(window, text=".", width= 5, height= 2, command= lambda: button_op ("."))
 
button_div = Button(window, text="/", width= 5, height= 2, command= lambda: button_op ("/"))
button_multi = Button(window, text="*", width= 5, height= 2, command= lambda: button_op ("*"))
button_add = Button(window, text="+", width= 5, height= 2, command= lambda: button_op ("+"))
button_subtr = Button(window, text="-", width= 5, height= 2, command= lambda: button_op ("-"))
button_equal = Button(window, text="=", width= 5, height= 2, command= lambda: make_op ())
 
 
#puts buttons in windows
button_erase.grid(row= 1 , column= 0 , padx= 5 , pady= 5)
button_paren1.grid(row= 1 , column= 1 , padx= 5 , pady= 5)
button_paren2.grid(row= 1, column= 2 , padx= 5 , pady= 5)
button_div.grid(row= 1, column= 3 , padx= 5 , pady= 5)
 
button9.grid(row= 2, column= 0 , padx= 5 , pady= 5)
button8.grid(row= 2, column= 1 , padx= 5 , pady= 5)
button7.grid(row= 2, column= 2 , padx= 5 , pady= 5)
button_multi.grid(row= 2, column= 3 , padx= 5 , pady= 5)
 
button6.grid(row= 3, column= 0 , padx= 5 , pady= 5)
button5.grid(row= 3, column= 1 , padx= 5 , pady= 5)
button4.grid(row= 3, column= 2 , padx= 5 , pady= 5)
button_add.grid(row= 3, column= 3 , padx= 5 , pady= 5)
 
button3.grid(row= 4, column= 0 , padx= 5 , pady= 5)
button2.grid(row= 4, column= 1 , padx= 5 , pady= 5)
button1.grid(row= 4, column= 2 , padx= 5 , pady= 5)
button_subtr.grid(row= 4, column= 3 , padx= 5 , pady= 5)
 
button0.grid(row= 5, column= 0 , columnspan= 2, padx= 5 , pady= 5)
button_dot.grid(row= 5, column= 2 , padx= 5 , pady= 5)
button_equal.grid(row= 5, column= 3 , padx= 5 , pady= 5)







window.mainloop()