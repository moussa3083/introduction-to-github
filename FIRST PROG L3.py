from tkinter import*

Myproject = Tk()
Myproject.title("First Prog")
Myproject.geometry("600x500")
Mylabel = Label(Myproject,text="web browser",fg="black",bg="white",font="helvatica 30 bold")
Mylabel.pack(pady=20)
Mybutton = Button(Myproject,text="exit",bg="#869190",fg="white",font="helvatica 22 bold",pady=2,command=exit)
Mybutton.pack(side = LEFT,anchor="ne",padx=3)
Mytext = Entry(Myproject)
Mytext.pack(side=LEFT,anchor="ne",ipady=100,ipadx=30)






Myproject.mainloop()

