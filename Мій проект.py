import tkinter as tk
import math

# Функція для зміни кольору фону
def change_bg(color):
    root.config(bg=color)
    entry.config(bg=color)
    frame.config(bg=color)
    # змінюємо фон для всіх кнопок
    for child in frame.winfo_children():
        child.config(bg=color)
        for btn in child.winfo_children():
            btn.config(bg=color)

def calculator():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def insert_numbers(value):
    entry.insert(tk.END, value)

def clear_entry():
    entry.delete(0, tk.END)

def percent():
    try:
        value = eval(entry.get())
        result = value / 100
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x400")


entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry.pack(fill="x", padx=10, pady=10)


frame = tk.Frame(root)
frame.pack()


buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "%", "C", "+"],
    ["="]
]

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(side="top", expand=True, fill="both")
    for btn in row:
        if btn == "=":
            button = tk.Button(row_frame, text=btn, font=("Arial", 18), width=5, height=2,
                               command=calculator)
        elif btn == "C":
            button = tk.Button(row_frame, text=btn, font=("Arial", 18), width=5, height=2,
                               command=clear_entry)
        elif btn == "%":
            button = tk.Button(row_frame, text=btn, font=("Arial", 18), width=5, height=2,
                               command=percent)
        else:
            button = tk.Button(row_frame, text=btn, font=("Arial", 18), width=5, height=2,
                               command=lambda b=btn: insert_numbers(b))
        button.pack(side="left", expand=True, fill="both")


menubar = tk.Menu(root)
color_menu = tk.Menu(menubar, tearoff=0)
colors = ["white", "lightgrey", "yellow", "lightblue", "pink", "green"]

for color in colors:
    color_menu.add_command(label=color, command=lambda c=color: change_bg(c))

menubar.add_cascade(label="Фон", menu=color_menu)
root.config(menu=menubar)

root.mainloop()
