from tkinter import *
import tkinter.messagebox as MessageBox
import pymysql
 
class deleteBook():
     
 def __init__(self, root):
        self.root = root
        self.root.title('DELETE BOOKS')
        self.root.resizable(False, False)
        self.root.geometry('600x600')
        self.root.config(bg="#BC8848")            
        self.headingFrame1 =Frame(root,bg="#BDA18A",bd=5)
        self.headingFrame1.place(relx=0.2,rely=0.05,relwidth=0.6,relheight=0.16)

        self.headingLabel =Label(self.headingFrame1, text="Welcome to \n AzAs Library", bg='#6c3a13', fg='#BC8848', font=('Courier',20))
        self.headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)  
        
        labelFrame = Frame(root,bg="#6c3a13")
        labelFrame.place(x=0,y=200,width=600,height=300)

        id = Label(root, text="Enter ID:", font=("verdana 15"),bg="#6c3a13",fg="#BC8848")
        id.place(x=30, y=300)
        self.id_entry = Entry(root, font=("verdana 15"))
        self.id_entry.place(x=150, y=300)
        btnDelete = Button(root, text="Delete", command=self.delete,bg="#BC8848",fg='#6c3a13', width=20,height=2, font=("verdana ",)).place(x=100, y=400)
        
        self.quit_button = Button(root,text="Quit", font=("verdana "), width=20,height=2, bg="#BC8848",fg='#6c3a13', command=root.destroy)
        self.quit_button.place(x=300, y=400)
  
 def delete(self):
    if(self.id_entry.get() == ""):
       MessageBox.showinfo("ALERT", "Please enter ID to delete row")
    else:
       con = pymysql.connect(host="localhost", user="root", password="", database="GES_BIBLIO")
       cursor = con.cursor()
       cursor.execute("delete from livre where idL='"+ self.id_entry.get() +"'")
       cursor.execute("commit")
       self.id_entry.delete(0, 'end')
      #  name_entry.delete(0, 'end')
      #  phone_entry.delete(0, 'end') 
       MessageBox.showinfo("Status", "Successfully Deleted")
       con.close()
       
root=Tk()
obj=deleteBook(root)
root.mainloop() 