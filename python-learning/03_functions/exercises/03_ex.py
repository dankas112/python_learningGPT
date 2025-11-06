# Задача 3. Четное или нечетное

# Создай функцию check_number(num), которая:

# принимает число;

# возвращает строку "четное" или "нечетное" в зависимости от числа.

def check_nember(num):
    if int(num) % 2 == 0:
        return 'четное'
    else:
        return 'нечетное'
    
print(check_nember(6))
print(check_nember(861))
print(check_nember(32))
print(check_nember(14))