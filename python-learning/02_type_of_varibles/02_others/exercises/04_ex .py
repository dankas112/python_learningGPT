# Задача 4 — Словарь

# Создай словарь с ключами: "name", "age", "city" и любыми значениями.

# Выведи все ключи

# Выведи все значения

# Добавь новый ключ "job"

# Удали ключ "city"

my_dict = {'name':'Svetlana', 'age':25, 'city': 'Alkatraz'}

print(my_dict.keys())
print(my_dict.values())

my_dict['job'] = 'trash strimer'
my_dict.pop('city')

print(my_dict.items())