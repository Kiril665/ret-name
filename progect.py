

point = 0


print("Привіт! Відповідай на кілька питань:")

# 1
num = input('1. Як мене звати?\n')
if num.lower() in ['kiril', 'кирил', 'кіріл']:
    print(f'молодець плюс{point+1}очко')
else:
    print(f'ні, ти шо минус{point-1}очко')

# 2
num2 = input('2. Скільки мені років?\n')
if num2 == '16':
    print(f'правильно плюс{point+1}очко')
else:
    print(f'неправильно минус{point-1}очко')

# 3
num3 = input('3. Моя улюблена мова програмування?\n')
if num3.lower() in ['c#', 'csharp']:
    print(f'красава плюс{point+1}очко')
else:
    print(f'не вгадав минус{point-1}очко')

# 4
num4 = input('4. Який колір я люблю?\n')
if num4.lower() in ['синій', 'blue']:
    print('вірно! плюс{point+1}очко')
else:
    print(f'ні, інший минус{point-1}очко')

# 5
num5 = input('5. Скільки буде 5 * 6?\n')
if num5 == '30':
    print(f'правильно! плюс{point+1}очко')
else:
    print(f'ні, 5*6 = 30 минус{point-1}очко')

# 6
num6 = input('6. Яка столиця України?\n')
if num6.lower() in ['київ', 'kyiv']:
    print(f'так! плюс{point+1}очко')
else:
    print(f'ні, це Київ минус{point-1}очко')

# 7
num7 = input('7. Python — це змія чи мова програмування?\n')
if num7.lower() in ['мова', 'мова програмування', 'програмування']:
    print(f'в точку! плюс{point+1}очко')
else:
    print(f'не зовсім минус{point-1}очко')

# 8
num8 = input('8. Яка цифра стоїть після 7?\n')
if num8 == '8':
    print(f'правильно плюс{point+1}очко')
else:
    print(f'неправильно минус{point-1}очко')

# 9
num9 = input('9. Який зараз рік?\n')
if num9 == '2025':
    print(f'молодець плюс{point+1}очко')
else:
    print(f'помилка минус{point-1}очко')

# 10
num10 = input('10. Скільки буде 2 + 2 * 2?\n')
if num10 == '6':
    print(f'вірно (порядок дій!) плюс{point+1}очко')
else:
    print(f'ні, правильна відповідь 6 минус{point-1}очко')

print(f'Кількість правильних відповідей {point}')
