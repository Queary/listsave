import eel

# list1:123321,list2:qweqwe,list3:test
#list2:qweqwe,list3:test


@eel.expose
def jspy(x):
    print('js-py:'+str(x))

@eel.expose
def savepy(id,text):
    print("savepy activition")
    f = open('data/list.txt','a',encoding='cp1251')
    # print(f.read())
    # f.write("qwe")
    f.write(str(id)+":"+str(text))
    f.write("\n")
    print(str(id)+":"+str(text))
    # print(f)

@eel.expose
def openpy():
    print("openpy activition")
    f = open('data/list.txt','r',encoding='cp1251')
    # print(f.read())
    # f.write("qwe").split
    text = f.read()
    text = text.split("\n")
    print(text)
    number = len(text)
    print(number)
    for number in range(number-1):
        print(text[number])
        if text[number] != '':
            te = text[number].split(":")
            eel.createjs(number,te[1])
        print(te[1])
    # print(ar[0])
    # print(f)

@eel.expose
def delpy(id):
    print("del activition")
    f = open('data/list.txt','r',encoding='cp1251')
    print(f)
    text = f.read().split("\n")
    print(text)
    lei = len(text)
    lei -=1
    print(lei)
    for value in range(lei):
        print(value)
        te = text[value].split(":")
        print(str(te)+"=="+str(id))
        if(te[0]) == id:
            text[value] = "";
        pass
    print(text)
    f = open('data/list.txt','w',encoding='cp1251')
    print(f)
    lei = len(text)
    lei -=1
    print(lei)
    for value in range(lei):
        print(value)
        print(str(text[value])+"!=''")
        if text[value] != None:
            f.write(text[value])
            f.write("\n")
        else:
            f.write()
        pass
    print(text)
    print("win")
    # print(f)

eel.init("interface")
eel.start("index.html",mode='chrome',size=(400,500))
