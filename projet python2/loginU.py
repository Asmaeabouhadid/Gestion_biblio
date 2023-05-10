import mysql.connector
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
#login for users

class LoginPage:
    def __init__(self):
        # création de la fenêtre principale
         self.root = Tk()
         self.root.title("Login form")
         self.root.geometry('600x600')
       
         backimage = Image.open("./imag/img2.png")
         self.backgrounPhoto = ImageTk.PhotoImage(backimage)
         self.background_label = Label(self.root, image=self.backgrounPhoto, bg="#5D340A")
         self.background_label.grid(row=0, column=0)
         self.background_label.place(x=0, y=0)
         self.root.resizable(False, False)
         self.root.title("login")
         self.frame = Frame(self.root, width=280, height=360, bg='white')
         self.frame.place(x=160, y=90)
         heading = Label(self.frame, text='Library', fg="#763613", bg='white', font="ariel 35 bold")
         heading.place(x=50, y=5)
         heading = Label(self.frame, text='Login', fg="#763613", bg='white', font="ariel 10 bold")
         heading.place(x=180, y=60)

        # Username label and entry
         self.username_entry = Entry(self.frame, width=25,fg='#AD956B', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
         self.username_entry.place(x=30, y=120)
         self.username_entry.insert(0, 'Username')
         self.username_entry.bind('<FocusIn>', self.on_enter_username)
         self.username_entry.bind("<FocusOut>", self.on_leave_username)
         Frame(self.frame, width=240, height=2, bg='#AD956B').place(x=25, y=150)

        # Password label and entry
         self.password_entry = Entry(self.frame, width=25, fg='#AD956B', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
         self.password_entry.place(x=30, y=200)
         self.password_entry.insert(0, 'Password')
         self.password_entry.bind('<FocusIn>', self.on_enter_password)
         self.password_entry.bind("<FocusOut>", self.on_leave_password)
         Frame(self.frame, width=240, height=2, bg='#AD956B').place(x=25, y=227)

        # Login button
         self.login_button = Button(self.frame, width=15, pady=8, text='Login', bg='#AD956B', fg='white', border=0, command=self.loginU)
         self.login_button.place(x=20, y=280)
         self.root = Tk()
         self.root.geometry("400x200")
         self.root.title("Login")
         
#  # Add account button 
         self.account_button = Button(self.frame, width=15, pady=8, text='Create account', bg='#AD956B', fg='white', border=0, command=self.open_signup)

         self.account_button.place(x=145, y=280) 

    def on_enter_username(self, event):
        self.username_entry.delete(0, 'end')

    def on_leave_username(self, event):
        if self.username_entry.get() == '':
            self.username_entry.insert(0, 'Username')

    def on_enter_password(self, event):
        self.password_entry.delete(0, 'end')

    def on_leave_password(self, event):
        if self.password_entry.get() == '':
            self.password_entry.insert(0, 'Password')

    # def check_credentials(self):
    #     # connexion à la base de données
    #     mydb = mysql.connector.connect(
    #         host="localhost",
    #         user="root",
    #         password="",
    #         database="GES_BIBLIO"
    #     )

    #     mycursor = mydb.cursor()

    #     # récupération des informations d'identification de la base de données
    #     query = "SELECT nom , passeword FROM users WHERE nom = %s AND password= %s"
    #     values = (self.username_entry.get(), self.password_entry.get())
    #     mycursor.execute(query, values)
    #     result = mycursor.fetchone()

        # vérification des informations d'identification
        # if result:
        #     # accès accordé - affichage d'un message de bienvenue
        #     messagebox.showinfo("Succès", "welcome, " + result[1] + "!")
        #     #self.root.destroy()

    def loginU(self):
         login.root.destroy() # Fermer la page de login
         from home2 import Menu
         Menu()

        # effacement des champs d'entrée
    # self.username_entry.delete(0, END)
    #     self.password_entry.delete(0, END)
    def open_signup(self):
        login.root.destroy() # Fermer la page de login
        from lsignup import Sign
        Sign() # Ouvrir la page d'inscription
if __name__ == '__main__':
     login = LoginPage()
     login.root.mainloop()