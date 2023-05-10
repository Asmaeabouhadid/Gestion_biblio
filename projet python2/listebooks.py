from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from tkinter import ttk

class Liste:
  def __init__(self, root):
      self.root = root
      self.root.title('LISTE OF BOOKS')
      self.root.resizable(False, False)
      self.root.geometry('600x600')
      self.root.config(bg="#BC8848")
      self.tree = ttk.Treeview(self.root)
      self.tree['columns'] = ('titre','year', 'auteur', 'image')

      self.headingFrame1 =Frame(root,bg="#6c3a13",bd=5)
      self.headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

      self.headingLabel =Label(self.headingFrame1, text="LIST OF BOOKS", bg='#6c3a13', fg='white', font=('Courier',20))
      self.headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)



        # colone d'indexe 
      self.tree.column('#0', width=0, stretch=NO)
      self.tree.column('titre', anchor=W, width=50)
      self.tree.column('year', anchor=W, width=150)
      self.tree.column('auteur', anchor=W, width=100)
      self.tree.column('image', anchor=CENTER, width=100)
      self.tree.heading('#0', text='', anchor=W)
      self.tree.heading('titre', text='TITLE', anchor=W)
      self.tree.heading('year', text='YEAR', anchor=W)
      self.tree.heading('auteur', text='AUTOR', anchor=W)
      self.tree.heading('image', text='PICTUR', anchor=CENTER)
      self.tree.place(x=50, y=160, width=482, height=374)
        
      self.display_data()

  def display_data(self):
        # connexion à la base de données
        con = pymysql.connect(host="localhost", user="root", password="", database="GES_BIBLIO")
        cursor = con.cursor()
        cursor.execute("SELECT titre,year,auteur,image FROM livre")
        
        # récupération des données
        rows = cursor.fetchall()
        
        # affichage des données dans le Treeview
        for row in rows:
            self.tree.insert('', END, values=row)

if __name__ == '__main__':
    root = Tk()
    Liste(root)
    root.mainloop()