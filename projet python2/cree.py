from tkinter import *
class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title('WHO ARE')
        self.root.resizable(False, False)
        self.root.geometry('600x600')
        self.root.config(bg="#BC8848")
        self.headingFrame1 =Frame(root,bg="#BDA18A",bd=5)
        self.headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
        self.headingLabel =Label(self.headingFrame1, text="Welcome to \n AzAs Library", bg='#6c3a13', fg='white', font=('Courier',20))
        self.headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
        admin_label = Label(root, text="LOGIN FOR ADMIN :", font=("Helvetica", 20), fg="#6c3a13",bg="#BC8848")
        admin_label.place(x=10, y=200)
        # Créer les boutons
        self.admin_button = Button(root, text="ADMIN", fg="#BC8848",width=20,height=2,bg="#6c3a13",command=self.admin).place(x=280,y=200)
        users_label = Label(root, text="LOGIN FOR USERS :", font=("Helvetica", 20), fg="#6c3a13",bg="#BC8848")
        users_label.place(x=10, y=300)
        self.user_button = Button(root, text="USERS",fg="#BC8848",width=20,height=2,bg="#6c3a13", command=self.users).place(x=290,y=300)

    def admin(self):
        self.root.destroy() 
        from login2 import LoginPage
        LoginPage()
    def users(self): 
      self.root.destroy() 
      from  loginU import LoginPage
      LoginPage()
root = Tk()
interface = Interface(root)
root.mainloop()