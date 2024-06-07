import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

class HeartAnimation:
    def __init__(self, root):
        self.root = root
        self.root.title("Mensaje Bonito")
        self.root.geometry("500x400")
        
        self.container = ttk.Frame(self.root)
        self.container.pack(fill=tk.BOTH, expand=True)
        
        self.message_label = ttk.Label(self.container, text="Te amo mucho ❤️", font=('Dancing Script', 20))
        self.message_label.pack(pady=20)

        self.center_image = Image.open("gato.jpg")
        self.center_photo = ImageTk.PhotoImage(self.center_image)
        self.image_label = ttk.Label(self.container, image=self.center_photo)
        self.image_label.pack(pady=20)

        self.heart_btn = ttk.Button(self.container, text="¡Corazones!", command=self.create_hearts)
        self.heart_btn.pack(pady=10)

    def create_hearts(self):
        for _ in range(10):
            heart_image = Image.open("corazon.png").convert("RGBA")  # Convertir la imagen a modo RGBA
            heart_image.thumbnail((30, 30))  # Redimensionar la imagen del corazón
            heart_photo = ImageTk.PhotoImage(heart_image)

            heart_label = ttk.Label(self.container, image=heart_photo)
            heart_label.photo = heart_photo
            heart_label.place(x=random.randint(0, 450), y=random.randint(0, 350))

            self.fall(heart_label)

    def fall(self, heart_label):
        x = random.randint(-5, 5)
        y = random.randint(1, 5)
        self.move(heart_label, x, y)

    def move(self, heart_label, x, y):
        x0, y0 = self.container.winfo_x() + heart_label.winfo_x(), self.container.winfo_y() + heart_label.winfo_y()
        x1, y1 = x0 + x, y0 + y

        if y1 < self.container.winfo_height():
            heart_label.place(x=x1, y=y1)
            self.root.after(50, self.move, heart_label, x, y)
        else:
            heart_label.destroy()

def main():
    root = tk.Tk()
    app = HeartAnimation(root)
    root.mainloop()

if __name__ == "__main__":
    main()
