import tkinter as tk
from tkinter import messagebox
import threading
import keyboard  # для гарячих клавіш
import mouse     # новий модуль для кліків
from PIL import Image, ImageTk



running = False  # стан автоклікера
delay = 0        # затримка між кліками (у мс)

# Вікно
window = tk.Tk()
window.geometry("600x400")
window.title("Auto Clicker")
window.configure(bg="#1e1e2f")
bg_image = Image.open("завантаження.webp")  # або .jpg
bg_image = bg_image.resize((600, 400))  # під розмір вікна
bg_photo = ImageTk.PhotoImage(bg_image)

# Створюємо Label для фону
bg_label = tk.Label(window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


# Заголовок
label = tk.Label(window, text="Auto Clicker", fg="#008080", bg="#D3D3D3", font=("Bakery", 16))
label.pack(pady=10)

# Поле вводу
entry = tk.Entry(window, fg="white", bg="black", width=20)
entry.place(x=200, y=100)

# Функція автокліку
def schedule_click():
    if running:
        mouse.click()  # тут реальний клік
        window.after(delay, schedule_click)

# Функція запуску
def start_clicker():
    global running, delay
    try:
        cps = int(entry.get())
        if cps <= 0:
            raise ValueError
        delay = int(1000 / cps)
        running = True
        messagebox.showinfo("Auto Clicker", f"Автоклікер запущено.\nЗатримка: {delay/1000:.3f} сек.")
        schedule_click()
    except ValueError:
        messagebox.showerror("Помилка", "Введіть ціле число більше нуля.")

# Функція зупинки
def stop_clicker():
    global running
    running = False
    messagebox.showinfo("Auto Clicker", "Автоклікер зупинено.")

# Функція для гарячої клавіші
def exit_app():
    global running
    running = False
    messagebox.showinfo("Auto Clicker", "Автоклікер зупинено.")
    window.destroy()

# Гаряча клавіша в окремому потоці
def hotkey_listener():
    keyboard.add_hotkey('esc', exit_app)
    keyboard.wait()

threading.Thread(target=hotkey_listener, daemon=True).start()

# Кнопки
start_btn = tk.Button(window, text="Запустити", fg="white", bg="#ff006e", font=("Arial", 16, "bold"), command=start_clicker)
start_btn.place(x=200, y=150)

stop_btn = tk.Button(window, text="Зупинити", fg="white", bg="blue", font=("Arial", 16, "bold"), command=stop_clicker)
stop_btn.place(x=350, y=150)

exit_btn = tk.Button(window, text="Вихід", fg="white", bg="red", font=("Arial", 14, "bold"), command=exit_app)
exit_btn.pack(pady=20)




window.mainloop()
