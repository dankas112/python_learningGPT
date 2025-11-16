# 4. namedtuple

# Задача:
# Создай структуру Person с полями name, age, city.
# Сделай 3 объекта и выведи:

# всех старше 18 лет

# список городов, где они живут

from collections import namedtuple

person = namedtuple("person", ['name', 'age', 'city'])
a = person('Andrew', 13, 'Moscow')
b = person('Boris', 20, 'Kirov')
c = person('Cora', 25, 'Vladivostok')

for x in a, b, c:
    if x.age >18:
        print(f'Пользователь {x.name} живет в {x.city}')