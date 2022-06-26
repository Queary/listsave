from tkinter import *

by = 0
sy = 30#40
texts = "";

def save():
    global window,text
    global sy
    print(texts)
    button['state'] = NORMAL
    gfd = greeting1.get()
    Lb = Label(text=gfd,justify=LEFT)
    sy+=20
    Lb.place(x=10,y=sy)
    pass

def click():
    global sy
    global window;
    global texts
    global greeting1
    #window.geometry("600x300")
    greeting1 = Entry()
    texts = greeting1.get()
    print(texts)
    btn = Button(text='save',command=save)
    btn.place(x=220,y=20)
    greeting1.place(x=110,y=20+5)
    button['state'] = DISABLED
    
    #greeting.destroy()

window = Tk()
window.geometry("300x400")
button = Button(text='add z',command=click)
button.pack()
window.mainloop()
