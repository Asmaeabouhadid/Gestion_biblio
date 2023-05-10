from tkinter import *

class Menu:
    def __init__(self, root):
        self.root = root
        self.root.title('Menu')
        self.root.resizable(False, False)
        self.root.geometry('600x600')
        self.root.config(bg="#BC8848")

        self.headingFrame1 = Frame(root, bg="#BDA18A", bd=5)
        self.headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

        self.headingLabel = Label(self.headingFrame1, text="Welcome to \n AzAs Library", bg='#6c3a13', fg='white', font=('Courier', 20))
        self.headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Créer les boutons pour les différentes options
        self.btn1 = Button(self.root, text=" listeUsers", bg='#6c3a13', fg='white', command=self.option1)
        self.btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

        self.btn2 = Button(self.root, text="searchbooks", bg='#6c3a13', fg='white', command=self.option2)
        self.btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

        self.btn3 = Button(self.root, text="listebooks", bg='#6c3a13', fg='white', command=self.option3)
        self.btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

        self.btn4 = Button(self.root, text="DeleteBook", bg='#6c3a13', fg='white', command=self.option4)
        self.btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

        self.btn5 = Button(self.root, text="addbook", bg='#6c3a13', fg='white', command=self.option5)
        self.btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

    def option1 (self):
        
        from listeUsers import User
        pass
        
    def option2(self):
        
        from searchbooks import BookSearchApp
        pass

    def option3(self):
        from listebooks import Liste
        Liste(root)
        pass

    def option4(self):
        from DeleteBook import deleteBook
        pass

    def option5(self):
        from addbook import AddBook
        pass

root = Tk()
menu = Menu(root)
root.mainloop()