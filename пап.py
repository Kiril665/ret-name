import tkinter as tk
from tkinter import messagebox

running = False  # стан автоклікера
delay = 0        # затримка між кліками (у мс)

# Вікно
window = tk.Tk()
window.geometry("600x400")
window.title("Auto Clicker")
window.configure(bg="#1e1e2f")

# Заголовок
label = tk.Label(window, text="Auto Clicker", fg="#008080", bg="#D3D3D3", font=("Bakery", 16))
label.pack(pady=10)

# Поле вводу
entry = tk.Entry(window, fg="white", bg="black", width=20)
entry.place(x=200, y=100)

# Функція автокліку
def schedule_click():
    if running:
        print("Клац!")  # тут можна вставити реальний клік pyautogui.click()
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

# Кнопки
start_btn = tk.Button(window, text="Запустити", fg="white", bg="#ff006e", font=("Arial", 16, "bold"), command=start_clicker)
start_btn.place(x=200, y=150)

stop_btn = tk.Button(window, text="Зупинити", fg="white", bg="blue", font=("Arial", 16, "bold"), command=stop_clicker)
stop_btn.place(x=350, y=150)

exit_btn = tk.Button(window, text="Вихід", fg="white", bg="red", font=("Arial", 14, "bold"), command=window.destroy)
exit_btn.pack(pady=20)

window.mainloop()
