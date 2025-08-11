# я не навиджу цей код нічого не працює а повино я переписував 2 рази



import tkinter as tk
import random


color = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "black", "white", "gray", "cyan", "magenta", "brown"
]



def random_colort():


     kdd = random.choice(color)

     button.config(highlightbackground=kdd, highlightcolor=kdd)


root = tk.Tk()
root.title("Рандомна рамка кнопки")
root.geometry("300x200")


button = tk.Button(root,text="Натисни на мене",command=random_colort,bd=5,relief="solid")

button.pack(pady=50)

root.mainloop()

