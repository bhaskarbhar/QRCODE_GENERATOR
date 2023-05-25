
#importing modules and tkinter library

import qrcode   
import random   
import smtplib  
from tkinter import * 
from tkinter import messagebox


#Creating Main window

top = Tk()
top.title("QR CODEGENERATOR")
top.geometry("600x600")
top.configure(bg="#338DF4")
bg=PhotoImage(file="C:\\Users\\Sukanta\\Desktop\\qrcode.png")
label=Label(top,image=bg)
label.place(relx=0.5, rely=0.5, anchor="center")
label7=Label(top,text="Username: ",font=("Arial", 15)).place(x=50,y=200)
label8=Label(top,text="Password: ",font=("Arial", 15)).place(x=50,y=260)
e1=Entry(top,width=30, font = ("Arial", 15),highlightthickness=5)
e1.config(highlightbackground = "#33E0FF", highlightcolor= "#33E0FF")
e1.place(x=150,y=200)
e2=Entry(top,show="*",width=30,font=("Arial", 15),highlightthickness=5) 
e2.config(highlightbackground = "#33E0FF", highlightcolor= "#33E0FF")
e2.place(x=150,y=260)


#creating login system
#data stored as text files

def login():
   a = e1.get()+"\n"
   b = e2.get()+"\n"
   if len(a)>1 and len(b)>1:
      username = open("C:\\Users\\Sukanta\\Desktop\\Usernames.txt")
      username_read = username.readlines()
      password = open("C:\\Users\\Sukanta\\Desktop\\passwords.txt")
      passwords_read= password.readlines()
      if a in username_read and b in passwords_read:
         u=username_read.index(a)
         p=passwords_read.index(b)
         if u==p:
            top1=Toplevel()#Creating QR CODE generation page
            top1.title("QR CODE GENERATOR")
            top1.geometry("602x602")
            top1.configure(bg="#dbd337")
            label1=Label(top1,text="Link:",font=("Arial", 15),bg="#dbd337").place(x=87,y=200)
            label2=Label(top1,text="QRcode\n name:",font=("Arial", 15),bg="#dbd337").place(x=60,y=240)
            e5 = Entry(top1, width=30, font=("Arial", 15), highlightthickness=5)
            e5.config(highlightbackground="#33E0FF", highlightcolor="#33E0FF")
            e5.place(x=135,y=200)
            e6 = Entry(top1, width=30, font=("Arial", 15), highlightthickness=5)
            e6.config(highlightbackground="#33E0FF", highlightcolor="#33E0FF")
            e6.place(x=135,y=250)
            def qr():   #creating qr code generation system
               global i
               img= qrcode.make(e5.get()+"")
               img.save(e6.get()+".png")
            qr_btn=Button(top1,text="GET QRCODE",command=qr).place(x=250,y=300)
         else:
            messagebox.showerror("Log in failed","Wrong username or password")
         username.close()
         password.close()
   else:
      messagebox.showwarning("ERROR","All fields are required")



#creating registration window and system
      
def register():
   top2=Toplevel()
   top2.title("REGISTRATION")
   top2.geometry("600x600")
   top2.configure(bg="#dbd337")
   e3 = Entry(top2, width=30, font=("Arial", 15), highlightthickness=5)
   e3.config(highlightbackground="#33E0FF", highlightcolor="#33E0FF")
   e3.place(x=130,y=170)
   e4 = Entry(top2, width=30, font=("Arial", 15), highlightthickness=5)
   e4.config(highlightbackground="#33E0FF", highlightcolor="#33E0FF")
   e4.place(x=130,y=230)
   e7 = Entry(top2, width=30, font=("Arial", 15), highlightthickness=5)
   e7.config(highlightbackground="#33E0FF", highlightcolor="#33E0FF")
   e7.place(x=130,y=290)
   e8 = Entry(top2, width=30, font=("Arial", 15), highlightthickness=5)
   e8.config(highlightbackground="#33E0FF", highlightcolor="#33E0FF")
   e8.place(x=130,y=350)

   #creating OTP system
   def otp():
      global number
      email= e7.get()+""
      number= str(random.randint(1000,9999))
      otp1="Your otp for registration in QR Code Generator is "+number #SSL means secure socket layer used for data encryption
      server= smtplib.SMTP_SSL("smtp.gmail.com",465)
      server.login(email_id,password) #Here emaild_id and password has been removed for security reasons. Give your email_id and password and quote them "".
      server.sendmail(email_id,email,otp1)
      server.quit()
   #user defined function for registration
   def register_file():
      n= e8.get()+""
      if n!=number:
         messagebox.showerror("Error","OTP didn't matched")
      else:
         global register
         register = open("C:\\Users\\Sukanta\\Desktop\\Usernames.txt","a")
         z=e3.get()+"\n"
         register.writelines(z)
         register.close()
         global password_new
         password_new= open("C:\\Users\\Sukanta\\Desktop\\passwords.txt","a")
         w= e4.get()+"\n"
         password_new.writelines(w)
         password_new.close()
         messagebox.showinfo("Registration","It's done")
   label9=Label(top2,text="REGISTRATION",font=("Arial", 36),bg="#dbd337").place(x=130,y=20)
   label3=Label(top2,text="Username:",font=("Arial", 15),bg="#dbd337").place(x=30,y=170)
   label4=Label(top2,text="Password:",font=("Arial", 15),bg="#dbd337").place(x=30,y=230)
   label5=Label(top2,text="Email_Id:",font=("Arial", 15),bg="#dbd337").place(x=40,y=290)
   label6=Label(top2,text="OTP:",font=("Arial", 15),bg="#dbd337").place(x=70,y=350)
   otp1=Button(top2, text="GET OTP", command=otp).place(x=280,y=410)
   registerbtn = Button(top2, text="Register", command=register_file).place(x=280,y=460)
b1=Button(top,text="LOG IN",height=1,width=20,command=login).place(x=250,y=320)
b2=Button(top,text="Register if new",height=1,width=20,command=register).place(x=250,y=350)
top.mainloop()

