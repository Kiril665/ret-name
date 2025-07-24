while True:
    print("\n=== КАЛЬКУЛЯТОР ===")
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    op = input("Оберіть операцію (+, -, *, /): ")

    if op == "+":
        print("Результат:", a + b)
    elif op == "-":
        print("Результат:", a - b)
    elif op == "*":
        print("Результат:", a * b)
    elif op == "/":
        if b != 0:
            print("Результат:", a / b)
        else:
            print("Помилка: ділення на нуль!")
    else:
        print("Невірна операція!")

    cont = input("Бажаєте продовжити? (так/ні): ").lower()
    if cont != "так":
        print("Калькулятор завершив роботу.")
        break
