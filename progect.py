import os

ret = input('ви хочете прочитатьть файл чи створить а потім прочитати')
print('1')
print('2')

if ret == '1':
 try:
        with open('C:/Users/Кирил/Desktop/windows.txt', 'r', encoding="utf-8") as filey :

         ret =    filey.read()
         print(ret)

 except FileNotFoundError:
     print('помилка')

elif ret == 2:

 os.mkdir('C:/Users/Кирил/Desktop/windows')
 with open('C:/Users/Кирил/Desktop/windows/myfile.txt', 'w', encoding="utf-8") as file:
    file.write("giga hacker 3000\n")

    with open('C:/Users/Кирил/Desktop/windows.txt', 'w', encoding="utf-8") as filey:
     filey.write("я хочу вже їсти\n")

     with open('C:/Users/Кирил/Desktop/windows.txt', 'r', encoding="utf-8") :

      ret = filey.read()
     print(ret)

else:

 print('я не розумію твою дію')