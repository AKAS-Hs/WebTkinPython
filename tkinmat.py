from tkinter import *

window=Tk()
window.geometry("260x350")
window.configure(bg="white")
window.title("CALC")

#label=Label(window,text="Akash")
#label.pack()
def helo():
    print("button clicked")
#button1.pack()

ent=Entry(window,width=38,borderwidth=5) #for the entry box
ent.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

button7 = Button(window, text="7", command=helo,width=5,height=2,bg="#BDBDBD")
button8 = Button(window, text="8", command=helo,width=5,height=2,bg="#BDBDBD")
button9 = Button(window, text="9", command=helo,width=5,height=2,bg="#BDBDBD")

button4 = Button(window, text="4", command=helo,width=5,height=2,bg="#BDBDBD")
button5 = Button(window, text="5", command=helo,width=5,height=2,bg="#BDBDBD")
button6 = Button(window, text="6", command=helo,width=5,height=2,bg="#BDBDBD")

button1 = Button(window, text="1", command=helo,width=5,height=2,bg="#BDBDBD")
button2 = Button(window, text="2", command=helo,width=5,height=2,bg="#BDBDBD")
button3 = Button(window, text="3", command=helo,width=5,height=2,bg="#BDBDBD")

buttondot = Button(window, text=".", command=helo,width=5,height=2,bg="#BDBDBD")
button0 = Button(window, text="0", command=helo,width=5,height=2,bg="#BDBDBD")
buttonequal = Button(window, text="=", command=helo,width=5,height=2,bg="#BDBDBD")

buttonplus = Button(window, text="+", command=helo,width=5,height=2,bg="#FFCC00")
buttonminus = Button(window, text="-", command=helo,width=5,height=2,bg="#FFCC00")
buttonmul = Button(window, text="x", command=helo,width=5,height=2,bg="#FFCC00")
buttondiv = Button(window, text="/", command=helo,width=5,height=2,bg="#FFCC00")

buttonAC = Button(window, text="AC", command=helo,width=15,height=2,bg="#BDBDBD")
buttondelete = Button(window, text="<=", command=helo,width=15,height=2,bg="#BDBDBD")


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