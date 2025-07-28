# main.py

import random
name = ['Кіріл','Кіра','Ілля','Дамір','Юля','Віка','Игарь']

def generate_name():
    return random.choice(name)


print("Випадкове ім'я:", generate_name())
