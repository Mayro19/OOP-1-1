from tkinter import *
window = Tk()

window.geometry("600x300+30+10")
window. title("Midterm in OOP")

lbl = Label(window, text="Enter your fullname: ", fg="red", font=("verdana", 10))
lbl.place(x=70,y=80)

txtfld = Entry(window, bd=3, font=("times new roman", 12))
txtfld.place(x=290, y=80)

txtfld2 = Entry(window, bd=3, font=("times new roman", 12))
txtfld2.place(x=290, y=150)

def clicked():
    value=txtfld.get()
    txtfld2.insert(END, str(value))

bttn= Button(window, text="Click to display your Fullname", fg="red", command=clicked)
bttn.place(x=70, y=150)


window.mainloop()
