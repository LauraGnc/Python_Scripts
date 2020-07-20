from tkinter import *

win = Tk()

win.title('Laura Gnc - Converter')
win.iconbitmap('icons8.png')
win.geometry('600x140')

def foo():
    var1_gm = float(var1.get()) * 1000
    var1_pd = float(var1.get()) * 2.204
    var1_ou = float(var1.get()) * 35.274

    t1.delete('1.0', END)
    t1.insert(END, var1_gm)
    t2.delete('1.0', END)
    t2.insert(END, var1_pd)
    t3.delete('1.0', END)
    t3.insert(END, var1_ou)

# This is the code for the Button 'Convert':
b1 = Button(win, activebackground='pink', text="Convert", command = foo)
b1.grid(row=0, column=2)

# This is the field to type the Kg, it will be stocked inside a variable:
var1 = StringVar()
e1 = Entry(win, textvariable = var1, font=('Helvetica', 18), width=5)
e1.grid(row=0, column=1)

# Write the text "Kg":
t4 = Label(win, text= 'Enter the kilogramme:')
t4.grid(row=0, column=0)

# This is the field for the output (ounce, grams, pounds):
t1 = Text(win, height = 1, width = 20)
t2 = Text(win, height = 1, width = 20)
t3 = Text(win, height = 1, width = 20)
t1.grid(row=3, column=0)
t2.grid(row=3, column=1)
t3.grid(row=3, column=2)

# This is the text to say which field correspond to what:
t5 = Label(win, text= 'Grams:')
t5.grid(row=2, column=0)

t6 = Label(win, text= 'Pounds:')
t6.grid(row=2, column=1)

t7 = Label(win, text= 'Ounces:')
t7.grid(row=2, column=2)

# This is the item that will make a blank line, to make the program looks clearer
space = Label(win, width=10)
space.grid(row=1, column=0)

win.mainloop()

