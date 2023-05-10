from tkinter import *
from tkinter import ttk
import pymysql

class User:
    def __init__(self, root):
        self.root = root
        self.root.title('LIST OF USERS')
        self.root.resizable(False, False)
        self.root.geometry('600x600')
        self.root.config(bg="#BC8848")
        self.headingFrame1 =Frame(root,bg="#BDA18A",bd=5)
        self.headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

        self.headingLabel =Label(self.headingFrame1, text="LIST OF USERS", bg='#6c3a13', fg='white', font=('Courier',20))
        self.headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
        self.tree = ttk.Treeview(self.root)
        self.tree['columns'] = ('Id','Nom', 'passeword', 'email')

        # colone d'indexe 
        self.tree.column('#0', width=0, stretch=NO)
        self.tree.column('Id', anchor=W, width=50)
        self.tree.column('Nom', anchor=W, width=150)
        self.tree.column('passeword', anchor=W, width=100)
        self.tree.column('email', anchor=CENTER, width=100)
        self.tree.heading('#0', text='', anchor=W)
        self.tree.heading('Id', text='ID', anchor=W)
        self.tree.heading('Nom', text='NAME', anchor=W)
        self.tree.heading('passeword', text='Passeword', anchor=W)
        self.tree.heading('email', text='Email', anchor=CENTER)
        self.tree.place(x=50, y=160, width=482, height=374)
        self.quit_button = Button(root,text="Quit",bg='#6c3a13', width=20,height=2, fg='black', command=root.destroy)
        self.quit_button.place(x=210, y=450)
        
        self.display_data()

    def display_data(self):
        # connexion à la base de données
        con = pymysql.connect(host="localhost", user="root", password="", database="GES_BIBLIO")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM users")
        
        # récupération des données
        rows = cursor.fetchall()
        
        # affichage des données dans le Treeview
        for row in rows:
            self.tree.insert('', END, values=row)

if __name__ == '__main__':
    root = Tk()
    User(root)
    root.mainloop()
