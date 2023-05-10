from tkinter import *
from PIL import Image, ImageTk
import os
import random

class ImageGrid:
    def __init__(self, root):
        self.root = root
        self.root.title('LIBRARY BOOKS')
        self.root.resizable(False, False)
        self.root.geometry('600x600')
        self.root.config(bg="#BC8848")      
        self.headingFrame1 = Frame(root, bg="#BDA18A", bd=5)
        self.headingFrame1.place(relx=0.2, rely=0.05, relwidth=0.6, relheight=0.16)

        self.headingLabel = Label(self.headingFrame1, text="Welcome to \n AzAs Library", bg='#6c3a13', fg='white', font=('Courier', 20))
        self.headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.image_dir = "./IMAGES"  # Le chemin vers le dossier contenant les images
        self.images_per_row = 4  # Nombre d'images par rangée
        self.images_per_page = 8  # Nombre total d'images à afficher

        # Obtenez tous les noms de fichiers dans le dossier images
        self.image_files = [f for f in os.listdir(self.image_dir) if os.path.isfile(os.path.join(self.image_dir, f))]

        # Créer un conteneur pour stocker toutes les images
        self.image_container = Frame(root, bg="#BC8848")
        self.image_container.place(x=40, y=200)

        # Afficher les images
        self.show_images()  # Afficher les images

    def show_images(self):
        # Effacer les images actuellement affichées
        for widget in self.image_container.winfo_children():
            widget.destroy()

        # Sélectionner les images à afficher
        selected_images = random.sample(self.image_files, self.images_per_page)

        # Afficher les images avec les titres correspondants
        for i, file_name in enumerate(selected_images):
            # Ouvrir le fichier image et le convertir en un objet PhotoImage Tkinter
            image_path = os.path.join(self.image_dir, file_name)
            image = Image.open(image_path)
            photo = ImageTk.PhotoImage(image)

            # Créer un widget Label pour afficher le titre de l'image
            title_label = Label(self.image_container, text=file_name.split(".")[0], bg="#BC8848")
            title_label.grid(row=i // self.images_per_row * 2, column=i % self.images_per_row, pady=(0, 5))

            # Créer un widget Label pour afficher l'image avec des marges
            image_label = Label(self.image_container, image=photo, bg="#BC8848")
            image_label.image = photo  # Garde une référence à l'objet PhotoImage pour éviter la suppression de la mémoire
            image_label.grid(row=i // self.images_per_row * 2 + 1, column=i % self.images_per_row, padx=10, pady=5)

root = Tk()
menu = ImageGrid(root)
root.mainloop()
