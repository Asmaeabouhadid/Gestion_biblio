from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector
class Sign:
    def __init__(self, root):
        self.root = root
        self.root.title('Sign Up')
        self.root.resizable(False,False)
        self.root.geometry('600x600')
        backimage = Image.open("./imag/img2.png")
        self.backgrounPhoto = ImageTk.PhotoImage(backimage)

        # Affichage de l'image sur un label
        self.background_label = Label(self.root, image=self.backgrounPhoto)
        self.background_label.pack()
     


        self.frame1 =Frame(self.root,width=280,height=360,bg='white')
        self.frame1.place(x=160,y=90)
        self.heading=Label(self.frame1,text='Library',fg="#AD956B",bg='white',font ="ariel 35 bold")
        self.heading.place(x=50,y=5)
        self.heading=Label(self.frame1,text='Sign Up',fg="#AD956B",bg='white',font ="ariel 10 bold")
        self.heading.place(x=180,y=60) 
        #   boutton ajouter                                                                                                                                                                                      

        signup_button = Button(self.frame1, width=25, pady=8, text='Sign Up', bg='#AD956B', fg='white', border=0 , command=self.enter)
        signup_button.place(x=40, y=307)
   

        # username
        self.user = Entry ( self.frame1,width=25,fg='#AD956B',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
        self.user.insert(0,'Username')
        self.user.place(x=30,y=80)
        self.user.bind('<Enter>', self.on_enter_user)
        self.user.bind('<Leave>', self.on_leave_user)
        Frame(self.frame1,width=240,height=2,bg='#AD956B').place(x=25,y=107)
        
        
        # email
        self.email = Entry(self.frame1,width=25,fg='#AD956B',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
        self.email.insert(0,'Email')
        self.email.place(x=30,y=140)
        self.email.bind('<Enter>', self.on_enter_email)
        self.email.bind('<Leave>', self.on_leave_email)
        Frame(self.frame1,width=240,height=2,bg='#AD956B').place(x=25,y=167)
        
        

        # password
        self.password=Entry(self.frame1,width=25,fg='#AD956B',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
        self.password.place(x=30,y=200)
        self.password.insert(0,'Password')
        self.password.bind('<Enter>', self.on_enter_password)
        self.password.bind('<Leave>', self.on_leave_password)
        Frame(self.frame1,width=240,height=2,bg='#AD956B').place(x=25,y=227)
        


        # confirm password
        self.confirm_pass=Entry(self.frame1,width=25,fg='#AD956B',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
        self.confirm_pass.place(x=30,y=260)
        self.confirm_pass.insert(0,'Confirm Your Password')
        self.confirm_pass.bind('<Enter>', self.on_enter_confirm_password)
        self.confirm_pass.bind('<Leave>', self.on_leave_confirm_password)
        Frame(self.frame1,width=240,height=2,bg='#AD956B').place(x=25,y=290)
            # enregistrer username
    def on_enter_user(self, e):
        self.user.delete(0,'end')

    def on_leave_user(self, e):
        if self.user.get()=='':
            self.user.insert(0,'Username')

    # enregistrer email
    def on_enter_email(self,e):
        self.email.delete(0,'end')

    def on_leave_email(self,e):
        if self.email.get()=='':
            self.email.insert(0,'Email')

    #enrigster password
    def on_enter_password(self,e):
        self.password.delete(0,'end')

    def on_leave_password(self,e):
        if self.password.get()=='':
            self.password.insert(0,'Password')

    #confirm password
    def on_enter_confirm_password(self,e):
        self.confirm_pass.delete(0,'end')

    def on_leave_confirm_password(self,e):
        if self.confirm_pass.get()=='':
            self.confirm_pass.insert(0,'Confirm Your Password')
        # ... same as before ...
       

    def enter(self):
        self.root.destroy()
        from home2 import Menu
        Menu()

root = Tk()
signup = Sign(root)
root.mainloop()
