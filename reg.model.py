from tkinter import *
import tkinter.messagebox as messageBox
import mysql.connector as mysql
   
window = Tk()
window.geometry("600x300")
window.title("Result-app")
window.iconbitmap("../path")
window.config(background='#41B77F')

Label_titel = Label(window, text="Welcome on our app", font=("courier", 35), bg= '#41B77F', fg='white')
Label_titel.pack()

id = Label(window,text='Enter id', font=('bold', 10))
id.place(x=20,y=30)

name = Label(window,text='Enter Name', font=('bold', 10))
name.place(x=20,y=60)

password = Label(window,text='Enter password', font=('bold', 10))
password.place(x=20,y=60)

Cours = Label(window,text='Enter Cours', font=('bold', 10))
Cours.place(x=20,y=90);

e_id = Entry()
e_id.place(x=150, y=30)

e_name = Entry()
e_name.place(x=150, y=60)

e_password = Entry()
e_password.place(x=150, y=60)

e_Cours = Entry()
e_Cours.place(x=150, y=90)

update = Button(window, text="Update", font=("italic", 10), bg="white", command=update)
update.place(x=20, y=140)

delect = Button(window, text="Delect", font=("italic", 10), bg="white", command=delect)
delect.place(x=20, y=140)

insert = Button(window, text="Insert", font=("italic", 10), bg="white", command=insert)
insert.place(x=20, y=140)

get = Button(window, text="Get", font=("italic", 10), bg="white", command=get)
get.place(x=190, y=140)

window.mainloop()