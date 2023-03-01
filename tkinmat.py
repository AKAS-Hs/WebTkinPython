from tkinter import *

window=Tk()
window.geometry("260x350")
window.configure(bg="white")
window.title("CALC")

#label=Label(window,text="Akash")
#label.pack()

#button1.pack()

ent=Entry(window,width=38,borderwidth=5) #for the entry box
ent.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

def button_click(number):
    #ent.delete(0,END)
    current=ent.get()
    ent.delete(0,END)
    ent.insert(0,str(current)+str(number))

def button_clear():
    ent.delete(0,END)

def button_delete():
    print(" ")

def button_add():
    first_number=ent.get()
    global f_num
    global math
    math="addition"
    f_num=int(first_number)
    ent.delete(0,END)

def button_sub():
    first_number=ent.get()
    global f_num
    global math
    math = "subtraction"
    f_num=int(first_number)
    ent.delete(0,END)

def button_mul():
    first_number=ent.get()
    global f_num
    global math
    math="multiplication"
    f_num=int(first_number)
    ent.delete(0,END)

def button_div():
    first_number=ent.get()
    global f_num
    global math
    math="division"
    f_num=int(first_number)
    ent.delete(0,END)

def button_equal():
    second_number=ent.get()
    ent.delete(0,END)
    if math == "addition":
        ent.insert(0, f_num+ int(second_number))

    if math == "subtraction":
        ent.insert(0,f_num-int(second_number))

    if math == "multiplication":
        ent.insert(0,f_num*int(second_number))

    if math == "division":
        ent.insert(0,f_num/int(second_number))





button7 = Button(window, text="7", command=lambda :button_click(7),width=5,height=2,bg="#BDBDBD")
button8 = Button(window, text="8", command=lambda : button_click(8),width=5,height=2,bg="#BDBDBD")
button9 = Button(window, text="9", command=lambda: button_click(9),width=5,height=2,bg="#BDBDBD")

button4 = Button(window, text="4", command=lambda :button_click(4),width=5,height=2,bg="#BDBDBD")
button5 = Button(window, text="5", command=lambda :button_click(5),width=5,height=2,bg="#BDBDBD")
button6 = Button(window, text="6", command=lambda :button_click(6),width=5,height=2,bg="#BDBDBD")

button1 = Button(window, text="1", command=lambda :button_click(1),width=5,height=2,bg="#BDBDBD")
button2 = Button(window, text="2", command=lambda :button_click(2),width=5,height=2,bg="#BDBDBD")
button3 = Button(window, text="3", command=lambda :button_click(3),width=5,height=2,bg="#BDBDBD")

buttondot = Button(window, text=".", command=lambda :button_click("."),width=5,height=2,bg="#BDBDBD")
button0 = Button(window, text="0", command=lambda :button_click(0),width=5,height=2,bg="#BDBDBD")
buttonequal = Button(window, text="=", command=button_equal,width=5,height=2,bg="#BDBDBD")

buttonplus = Button(window, text="+", command=button_add,width=5,height=2,bg="#FFCC00")
buttonminus = Button(window, text="-", command=button_sub,width=5,height=2,bg="#FFCC00")
buttonmul = Button(window, text="x", command=button_mul,width=5,height=2,bg="#FFCC00")
buttondiv = Button(window, text="/", command=button_div,width=5,height=2,bg="#FFCC00")

buttonAC = Button(window, text="AC", command=button_clear,width=15,height=2,bg="#BDBDBD")
buttondelete = Button(window, text="<=", command=lambda: button_delete(),width=15,height=2,bg="#BDBDBD")


button7.grid(row=1,column=0,padx=5,pady=1)
button8.grid(row=1,column=1,padx=10,pady=10)
button9.grid(row=1,column=2,padx=10,pady=10)

button4.grid(row=2,column=0,padx=10,pady=10)
button5.grid(row=2,column=1,padx=10,pady=10)
button6.grid(row=2,column=2,padx=10,pady=10)

button1.grid(row=3,column=0,padx=10,pady=10)
button2.grid(row=3,column=1,padx=10,pady=10)
button3.grid(row=3,column=2,padx=10,pady=10)

buttondot.grid(row=4,column=0,padx=10,pady=10)
button0.grid(row=4,column=1,padx=10,pady=10)
buttonequal.grid(row=4,column=2,padx=10,pady=10)

buttonplus.grid(row=1,column=3,padx=10,pady=10)
buttonminus.grid(row=2,column=3,padx=10,pady=10)
buttonmul.grid(row=3,column=3,padx=10,pady=10)
buttondiv.grid(row=4,column=3,padx=10,pady=10)

buttonAC.grid(row=5,column=0,columnspan=2,padx=10,pady=10)
buttondelete.grid(row=5,column=2,columnspan=2,padx=2,pady=10)




window.mainloop()