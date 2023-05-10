from tkinter import *
import tkinter as tk
import mysql.connector

class BookSearchApp:

    def __init__(self, root):
        self.root = root
        root.title("SEARCH BOOKS")
        self.root.resizable(False, False)
        self.root.geometry('600x600')
        self.root.config(bg="#BC8848")
        labelFrame = Frame(root,bg="#6c3a13")
        labelFrame.place(x=10,y=200,width=600,height=300)

 
        self.headingFrame1 =Frame(root,bg="#6c3a13",bd=5)
        self.headingFrame1.place(relx=0.2,rely=0.05,relwidth=0.6,relheight=0.16)

        self.headingLabel =Label(self.headingFrame1, text="Welcome to \n AzAs Library", bg='#6c3a13', fg='#BC8848', font=('Courier',20))
        self.headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)       

        # Création des widgets pour la recherche
        self.title_label = Label(root, text="TITLE:",bg="#6c3a13",fg="#BC8848",font=("Helvetica", 20))
        self.title_entry = Entry(root)
        self.year_label = Label(root, text="YEAR:",bg="#6c3a13",fg="#BC8848",font=("Helvetica", 20))
        self.year_entry = Entry(root)
        self.author_label = Label(root, text="AUTHOR:",bg="#6c3a13",fg="#BC8848",font=("Helvetica", 20))
        self.author_entry = Entry(root)

        self.search_button = Button(root, text="SEARCH", bg='#BC8848', width=20,height=2, fg='#6c3a13',command=self.search)

        # Placement des widgets dans la fenêtre
        self.title_label.place(x=20, y=250)
        self.title_entry.place(x=150, y=260)
        self.year_label.place(x=20, y=300)
        self.year_entry.place(x=150, y=310)
        self.author_label.place(x=20, y=350)
        self.author_entry.place(x=150, y=360)
        
        self.search_button.place(x=50, y=440)
        self.quit_button = Button(root,text="Quit",bg='#BC8848', width=20,height=2, fg='#6c3a13', command=root.destroy)
        self.quit_button.place(x=240, y=440)
        

        # Connexion à la base de données
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="GES_BIBLIO"
        )

    def search(self):
        # Récupération des valeurs des champs de recherche
        title = self.title_entry.get()
        author = self.author_entry.get()
        year = self.year_entry.get()

        # Création de la requête SQL en fonction des champs remplis
        if title and author and year:
            query = "SELECT * FROM livre WHERE titre=%s AND auteur=%s AND annee=%s"
            values = (title, author, year)
        elif title and author:
            query = "SELECT * FROM livre WHERE titre=%s AND auteur=%s"
            values = (title, author)
        elif title and year:
            query = "SELECT * FROM livre WHERE titre=%s AND year=%s"
            values = (title, year)
        elif author and year:
            query = "SELECT * FROM livre WHERE auteur=%s AND year=%s"
            values = (author, year)
        elif title:
            query = "SELECT * FROM livre WHERE titre=%s"
            values = (title,)
        elif author:
            query = "SELECT * FROM livre WHERE auteur=%s"
            values = (author,)
        elif year:
            query = "SELECT * FROM livre WHERE year=%s"
            values = (year,)
        else:
            # Aucun champ rempli, on ne fait rien
            return

        # Exécution de la requête SQL
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        result = cursor.fetchone()

        # Affichage du résultat
        if result:
            book_id, title, author, year, image_path = result
            # Affichage du livre avec son image
            # TODO: compléter avec le code d'affichage de l'image
            print(f"WE FOUND THE BOOK \n THE TITLE is : {title} \n YEAR  IS :  {author}  \n  AND HIS  AUTHOR IS :{year}")
        else:
             print("No books found")
           
root = Tk()
app = BookSearchApp(root)
root.mainloop()
            