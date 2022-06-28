from tkinter import *

i = 0;
#larr= []; label arr
arr = [];
by = 0
sy = 60#40 #30
texts = "";
ras = 30#расстояние между списками

def delete(ii):
    global i
    global ras
    global sy
    global arr
    print("sy")
    print(sy)
    sy-=ras
    #i-=2;#баг
    print("delete")
    print(ii)
    arr[ii].destroy()
    arr[ii+1].destroy()
    print(len(arr))
    print(arr)
    arr.splice(ii,2)
    if len(arr) > 0 and ii != len(arr):
        print("if")
        print(arr[ii+2].command)
        arr[ii+2].configure(text = 'delete',command=lambda: delete(ii-2))
    
    pass

def save():
    global window
    global text
    global sy
    global btn
    global greeting1
    global arr
    global i
    global ras
    print("save")
    print(i)
    button['state'] = NORMAL
    gfd = greeting1.get()
    #Label(text=gfd,justify=LEFT) - раньше будут тут
    sy+=ras
    #btndel = Button(text='delete',command=save)
    
    #print(i)
    tx = i
    print("tx")
    print(tx)
    arr.append(Button(text = 'delete',command=lambda: delete(tx)))
    arr.append(Label(text=gfd))
    print(arr)
    #Lb.place(x=50,y=sy)
    #btndel.place(x=10,y=sy)
    arr[i].place(x=10,y=sy)
    arr[i+1].place(x=50,y=sy)
    btn.destroy()
    greeting1.destroy()
    i+=2;
    pass

def add():
    global sy
    global window;
    global texts
    global greeting1
    global btn
    #window.geometry("600x300")
    greeting1 = Entry()
    texts = greeting1.get()
    print(texts)
    btn = Button(text='save',command=save)
    #sy+=30
    btn.place(x=120,y=30)
    greeting1.place(x=10,y=30+3)
    button['state'] = DISABLED
    
    #greeting.destroy()

window = Tk()
window.geometry("300x400")
button = Button(text='add z',command=add)
button.pack()
window.mainloop()
