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
        self.btn2 = Button(self.root, text="BOOKS OF LIBRARY ", bg='#6c3a13', fg='white', command=self.option2)
        self.btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

        self.btn3 = Button(self.root, text="Search Books", bg='#6c3a13', fg='white', command=self.option3)
        self.btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

        self.btn4 = Button(self.root, text="LOG OUT", bg='#6c3a13', fg='white', command=root.destroy)
        self.btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

 
    def option3(self):
        from searchbooks import BookSearchApp
        pass

    def option2(self):
        from bookLibrary import ImageGrid
        ImageGrid()
        # pass



root = Tk()
menu = Menu(root)
root.mainloop()