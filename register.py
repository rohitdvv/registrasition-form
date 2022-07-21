from tkinter import *
import tkinter.messagebox as msg
r = Tk()
r.title("Welcome to LikeGeeks app")
r.geometry('1000x700')
r.configure(bg="#454545")

def clicked():
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",port=3306,user="root",password="Rohit@4878",
                           database='register')
    mycursor = mydb.cursor()
    username=unbox.get()
    password=pbox.get()
    emailid=ebox.get()
    mycursor.execute("insert into registration values(%s,%s,%s)",(username,password,emailid))
    mydb.commit()    
    msg.showinfo("Registration","Registered Sucessesful")
    
    

heading=Label(r,text="Registration Form",bg="#454545",fg="white",font=("bold",45))
heading.place(x=250,y=50)

username=Label(r,text="User Name :",bg="#454545",fg="white",font=("bold",30))
username.place(x=100,y=150)

unbox=Entry(r,width=60)
unbox.place(x=400,y=168)

password=Label(r,text="Password   :",bg="#454545",fg="white",font=("bold",30))
password.place(x=100,y=250)

pbox=Entry(r,width=60)
pbox.place(x=400,y=268)

email=Label(r,text="Email id   :",bg="#454545",fg="white",font=("bold",30))
email.place(x=100,y=350)

ebox=Entry(r,width=60)
ebox.place(x=400,y=368)

btn=Button(text="Register",width=20,bg="#C0C0C0",fg="white",command = clicked)
btn.place(x=400,y=468)


r.mainloop()
