# 1️⃣ Создай собственный модуль

# Создай файл my_utils.py и добавь туда функции:

# square(x) — возвращает x²

# is_even(x) — True/False

# greet(name) — печатает «Привет, <name>»

# В файле main.py импортируй модуль и вызови все функции.

def square(x):
    return x*x

def is_even(x):
    if x % 2:
        return False
    else:
        return True

def greet(name):
    print(f'Привет, {name}')
    
