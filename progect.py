print('ведіть список фільмів')
ret = input('1: ')
ret2 = input('2: ')
ret3 = input('3: ')
ret4 = input('4: ')
ret5 = input('5: ')
write = [ret, ret2, ret3, ret4, ret5]

print('\nВаш список фільмів:')
print('1.', write[0])
print('2.', write[1])
print('3.', write[2])
print('4.', write[3])
print('5.', write[4])

det = input('\nЩо ви хочете зробити (видалити,змінити або додати)? ').strip().lower()

# Видалення завдання
if det == 'видалити':
    delete_num = input('Введіть номер фільму, якій потрібно видалити (1-5): ')
    if delete_num.isdigit():
        num = int(delete_num)
        if 1 <= num <= 5:
            write[num - 1] = "[Видалено]"
            print(f"Завдання {num} видалено.")
        else:
            print("Такого номера немає.")
    else:
        print("Це не число!")

# Редагування завдання
elif det == 'змінити':
    editnum = input('Введіть номер завдання, яке хочете змінити (1-5): ')
    if editnum.isdigit():
        num2 = int(editnum)
        if 1 <= num2 <= 5:
            new_text = input('Введіть новий текст завдання: ')
            write[num2 - 1] = new_text
            print("Завдання змінено.")
        else:
            print("Такого номера на жаль немає.")
    else:
        print("Це не число!")

else:
     print("Незрозуміла дія.")

if det =='додати':

 name =input('ведіть фільм який хочете додати').strip()

 if name:

  write.append(name)
 print(f'фільм {name} додано')


else:

 print('назва фільму не може бути порожньою')



# Показати фінальний список
print('\nОновлений список завдань:')
print(write)

