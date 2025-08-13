import tkinter as tk

# Вікно
window = tk.Tk()
window.geometry("1000x1000")
window.title("Auto cliker")
window.configure(bg="#1e1e2f")

# Заголовок
label = tk.Label(window, bg="#D3D3D3", text="auto cliker", fg="#008080", font=("Bakery", 16))
label.pack(pady=10)

# Поле вводу
entry = tk.Entry(window, fg="white", bg="black", width=30)
entry.place(x=400, y=100)

output_label = tk.Label(window, text="", fg="yellow", bg="#1e1e2f", font=("Arial", 14))
output_label.pack(pady=10)

# Функція виводу
def text():
    tex = entry.get()
    output_label.config(text=f"Ви вели:{tex}")

# Кнопка
but = tk.Button(
    window,
    text="Вивести текст",
    fg="white",
    bg="#ff006e",
    font=("Arial", 19, "bold"),
    command=text,


)





but.place(x=400, y=150)

window.mainloop()
