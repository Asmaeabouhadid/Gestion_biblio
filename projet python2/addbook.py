# from tkinter import *
# from tkinter import filedialog
# from PIL import ImageTk, Image
# import pymysql
# from tkinter import messagebox

# class Add_book:
#     def __init__(self, root):
#         self.root = root
#         self.root.title('ADD BOOKS')
#         self.root.resizable(False, False)
#         self.root.geometry('600x600')
#         self.root.config(bg="#AD956B")
        
#         self.filename = None
        
#         headingFrame1 = Frame(root,bg="black",bd=5)
#         headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

#         headingLabel = Label(headingFrame1, text="Add Books", bg='#312509', fg='white', font=('Courier',15))
#         headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
#         labelFrame = Frame(root,bg="black")
#         labelFrame.place(x=10,y=200,width=600,height=300)
        
#         titre_label = Label(root, text="TITLE:", font=("Helvetica", 20), fg="#312509",bg="black")
#         titre_label.place(x=10,y=210)
#         self.ecr_titre = Entry(root, font=("Helvetica",15 ))
#         self.ecr_titre.place(x=160, y=210)

#         auteur_label = Label(root, text="AUTHOR:", font=("Helvetica", 20), fg="#312509",bg="black")
#         auteur_label.place(x=10,y=280)
#         self.ecr_auteur = Entry(root, font=("Helvetica", 15))
#         self.ecr_auteur.place(x=160, y=285)

#         annee_label = Label(root, text="YEAR:", font=("Helvetica", 20), fg="#312509",bg="black")
#         annee_label.place(x=10, y=350)
#         self.ecr_annee = Entry(root, font=("Helvetica", 15))
#         self.ecr_annee.place(x=160, y=355)

#         image_entry = Label(root, text="PICTURE:", font=("Helvetica", 20), fg="#312509",bg="black")
#         image_entry.place(x=10, y=400)
#         self.image_button = Button(root, width=15, height=1, command=self.selectionner_image, text="Upload image", fg="black")
#         self.image_button.place(x=160, y=412)

#         ajouter_button = Button(root, width=20, height=2, command=self.formulaire, text="ADD")
#         ajouter_button.place(x=120, y=455)

#         quitBtn = Button(root,text="Quit",bg='#f7f1e3', width=20,height=2, fg='black', command=root.destroy)
#         quitBtn.place(x=300, y=455)


#     def selectionner_image(self):
#         f_type = [("Png files", "*.png")]
#         self.filename = filedialog.askopenfilename(filetypes=f_type)
#         if self.filename:
#             img = Image.open(self.filename)
#             img = img.resize((100, 100))
#             self.img = ImageTk.PhotoImage(img)
#             label = Label(root, image=self.img_data, width=100, height=100)
#             label.place(x=400, y=250)

#     def formulaire(self):
#       try:
#         con = pymysql.connect(host="localhost", user="root", password="", database="GES_BIBLIO")
#         cur = con.cursor()
#         cur.execute("SELECT * FROM livre WHERE titre=%s", self.ecr_titre.get())
#         row = cur.fetchone()
#         if row is not None:
#          messagebox.showerror("Erreur", "Ce titre existe déjà", parent=self.root)
#         else:
#          with open(self.filename, 'rb') as f:
#             data = f.read()
#         cur.execute("INSERT INTO livre (titre, year, auteur, image) VALUES (%s, %s, %s, %s)",
#                     (self.ecr_titre.get(), self.ecr_annee.get(), self.ecr_auteur.get(), data))
#         con.commit()
#         messagebox.showinfo("Succès", "Le livre a été ajouté avec succès.", parent=self.root)
#         con.close()
#       except Exception as e:
#        messagebox.showerror("Erreur", f"Erreur de connexion : {str(e)}", parent=self.root)

# root=Tk()
# obj=Add_book(root)
# root.mainloop()                

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector

class AddBook:
    def __init__(self, root):
        self.root = root
        self.root.title('ADD BOOKS')
        self.root.resizable(False, False)
        self.root.geometry('600x600')
        self.root.config(bg="#BC8848")
        
        labelFrame = Frame(root,bg="#6c3a13")
        labelFrame.place(x=10,y=200,width=600,height=300)


        self.headingFrame1 =Frame(root,bg="#6c3a13",bd=5)
        self.headingFrame1.place(relx=0.2,rely=0.05,relwidth=0.6,relheight=0.16)

        self.headingLabel =Label(self.headingFrame1, text="Welcome to \n AzAs Library", bg='#BC8848', fg='white', font=('Courier',20))
        self.headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

        #Set up the layout
        self.id_label = Label(root, text="ID:",bg="#6c3a13",fg="#BC8848",font=("Helvetica", 20))
        self.id_label.place(x=10,y=200)

        self.id_entry = Entry(root)
        self.id_entry.place(x=100,y=210)

        self.title_label = Label(root, text="Title:",bg="#6c3a13",fg="#BC8848",font=("Helvetica", 20))
        self.title_label.place(x=10,y=250)

        self.title_entry = Entry(root)
        self.title_entry.place(x=100,y=260)

        self.year_label = Label(root, text="Year:",bg="#6c3a13",fg="#BC8848",font=("Helvetica", 20))
        self.year_label.place(x=10,y=300)

        self.year_entry = Entry(root)
        self.year_entry.place(x=100,y=310)

        self.author_label = Label(root, text="Author:",bg="#6c3a13",fg="#BC8848",font=("Helvetica", 20))
        self.author_label.place(x=10,y=350)

        self.author_entry = Entry(root)
        self.author_entry.place(x=100,y=360)
        self.image_label = Label(root, text="Image:",bg="#6c3a13",fg="#BC8848",font=("Helvetica", 20))
        self.image_label.place(x=10,y=400)

        self.image_button = Button(root, text="Select Image", fg='#BC8848', command=self.select_image)
        self.image_button.place(x=110,y=410)

        self.add_button = Button(root, text="Add Book",bg='#BC8848',width=20,height=2, fg='#6c3a13', command=self.add_book)
        self.add_button.place(x=50,y=450)

        self.quit_button = Button(root,text="Quit",bg='#BC8848', width=20,height=2, fg='#6c3a13', command=root.destroy)
        self.quit_button.place(x=300, y=450)

    def select_image(self):
        self.filename = filedialog.askopenfilename(initialdir="./", title="Select Image", filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg")))
        self.image = ImageTk.PhotoImage(Image.open(self.filename))
        self.image_label = Label(self.master, image=self.image)
        self.image_label.grid(row=6, column=0, columnspan=2)

    def add_book(self):
    # Get the values from the input fields
      id = self.id_entry.get()
      title = self.title_entry.get()
      year = self.year_entry.get()
      author = self.author_entry.get()

    # Convert the image to binary data
      with open(self.filename, "rb") as f:
        image_data = f.read()

    # Insert the book into the database
      connection = mysql.connector.connect(host="localhost", user="root", password="", database="GES_BIBLIO")
      cursor = connection.cursor()
      sql = "INSERT INTO livre (idL, titre, year, auteur, image) VALUES (%s, %s, %s, %s, %s)"
      values = (id, title, year, author, image_data)
      cursor.execute(sql, values)
      connection.commit()

    # Clean up
      cursor.close()
      connection.close()

    # Clear the input fields
      self.id_entry.delete(0, END)
      self.title_entry.delete(0, END)
      self.year_entry.delete(0, END)
      self.author_entry.delete(0, END)

    # Display a message box
      messagebox.showinfo("Success", "Book added successfully.")

root = Tk()
app = AddBook(root)
root.mainloop()