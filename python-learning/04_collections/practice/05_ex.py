# 5. OrderedDict

# Задача:
# Сделай программу, которая сохраняет порядок добавления товаров в корзину.
# Пусть пользователь вводит товар и количество (до stop).
# Выведи их в порядке добавления.

from collections import OrderedDict
groceries_dict = OrderedDict()

while True:
    user_input = str(input("Введите пару вида: 'товар'-'пробел'-'количество': "))
    user_list = user_input.split()
    if user_input == "стоп":
        break
    elif len(user_list) != 2:
        print('Некоректный ввод! Попробуйте еще раз!')
    else:
        groceries_dict[user_list[0]] = user_list[1]
        print('Товар добавлен!')

for x in groceries_dict.keys():
    print(f'{x} : {groceries_dict[x]}')
    
# OrderedDict — Работает, но есть нюанс

# В Python 3.7+ обычный словарь и так сохраняет порядок → OrderedDict уже не нужен.

# Но раз задача тренировка — всё норм.

# ❗ Ошибка логики:

# Ты перезаписываешь количество товара, вместо добавления.

# Если пользователь введёт:

# яблоки 2
# яблоки 3


# То результат будет 3, а не [2, 3] или 5.

# ✔ Вариант 1: перезаписывать (как сейчас)

# Ок.

# ✔ Вариант 2: хранить список количеств:
# groceries_dict = OrderedDict()

# ...
# if item not in groceries_dict:
#     groceries_dict[item] = []
# groceries_dict[item].append(int(amount))

# ✔ Вариант 3: суммировать:
# groceries_dict[item] = groceries_dict.get(item, 0) + int(amount)