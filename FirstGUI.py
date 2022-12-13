from tkinter import *
from tkinter import messagebox

'''root = Tk()
root.title("Login Info")
root.geometry("320x220")
name = Label(root, text="Enter User Id").place(x=10, y=10)

password=Label(root, text="Enter Password").place(x=10, y=40)

t1 = Entry(root)
t1.place(x=140, y=10)
t2 = Entry(root)
t2.place(x=140, y=40)
t2.config(show="*")

Button(text="Login", height=1, width=5).place(x=100, y=80)
Button(text="Rest", height=1, width=5).place(x=150, y=80)
root.mainloop()'''

root = Tk()
root.title("New User Information")
root.geometry("280x200")
root.config(bg='sky blue')
name = Label(root, text="Enter User Id", bg='sky blue').place(x=10, y=10)

passw = Label(root, text="Enter Password", bg='sky blue').place(x=10, y=50)
confp = Label(root, text="Confirm Password", bg='sky blue').place(x=10, y=90)


t1 = Entry(root)
t1.place(x=10, y=30)
t2 = Entry(root)
t2.place(x=10, y=70)
t2.config(show="*")
t3 = Entry(root)
t3.place(x=10, y=110)
t3.config(show="*")

Button(text="Submit", height=1, width=6).place(x=20, y=150)
Button(text="Reset", height=1, width=6).place(x=90, y=150)

root.mainloop()