from tkinter import *

a = Tk()
a.title('window')
a.geometry('500x500+300+100')
b = StringVar()  #this will store value of textbox


def com():
    c = b.get()
    lab12 = Label(text=c, font=20).pack()


labl1 = Label(text='Torrence is gay', font=30).pack()

button1 = Button(text='Press to count', command=com).pack()

text = Entry(textvariable=b).pack()

a.mainloop()