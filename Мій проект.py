import customtkinter as ctk
from tkinter import messagebox
import os

# Отримати шлях до Робочого столу
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "users.txt")


# Функція для збереження даних
def save_data():
    username = entry_username.get()
    password = entry_password.get()

    if username and password:
        with open(desktop_path, "a") as file:
            file.write(f"Username: {username}, Password: {password}\n")
        messagebox.showinfo("Успіх", f"Дані збережено на Робочому столі!")
        entry_username.delete(0, ctk.END)
        entry_password.delete(0, ctk.END)
    else:
        messagebox.showwarning("Помилка", "Заповніть всі поля!")


# --- Вікно ---
window = ctk.CTk()
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

window.geometry("400x350")
window.title("Сторінка логіна")

# --- Заголовок ---
label = ctk.CTkLabel(window, text="Введіть ваші дані", font=("Bakery", 20))
label.pack(pady=25)

# --- Поля вводу ---
entry_username = ctk.CTkEntry(window, placeholder_text="Username", width=250)
entry_username.pack(pady=10)

entry_password = ctk.CTkEntry(window, placeholder_text="Password", show="*", width=250)
entry_password.pack(pady=10)

# --- Кнопка увійти ---
login_button = ctk.CTkButton(window, text="Увійти", width=100, command=save_data)
login_button.pack(pady=25)

window.mainloop()
