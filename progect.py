import os


FILE = r"C:\\Users\\Кирил\\справи.txt"

# Створює файл, якщо його немає
def init():
    if not os.path.exists(FILE):
        open(FILE, "w", encoding="utf-8").close()

def показати():
    with open(FILE, "r", encoding="utf-8") as f:
        справи = f.readlines()
    if not справи:
        print("Справ немає.")
    else:
        for i, s in enumerate(справи, 1):
            print(f"{i}. {s.strip()}")

def додати():
    справа = input("Додати справу: ")
    with open(FILE, "a", encoding="utf-8") as f:
        f.write(справа + "\n")
    print("Додано.")

def очистити():
    open(FILE, "w", encoding="utf-8").close()
    print("Очищено.")

def видалити():
    with open(FILE, "r", encoding="utf-8") as f:
        справи = f.readlines()
    if not справи:
        print("Справ немає.")
        return
    показати()

    n = input("Номер справи для видалення: ")
    if n.isdigit():
        n = int(n)
        if 1 <= n <= len(справи):
            видалена = справи.pop(n - 1)
            with open(FILE, "w", encoding="utf-8") as f:
                f.writelines(справи)
            print(f"Видалено: {видалена.strip()}")
        else:
            print("Неправильний номер.")
    else:
        print("Введіть число.")

def меню():
    init()
    while True:
        print("\n1 - Показати\n2 - Додати\n3 - Очистити\n4 - Видалити\n5 - Вийти")
        c = input("> ")
        if c == "1": показати()
        elif c == "2": додати()
        elif c == "3": очистити()
        elif c == "4": видалити()
        elif c == "5": break
        else: print("Спробуйте ще раз.")

меню()