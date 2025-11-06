# Задача 5: Фильтрация списка

# Дан список чисел [3, 6, 1, 9, 2, 8, 4]

# Создать новый список, в который попадут только числа больше 4

# Вывести новый список

numbers = [3, 6, 1, 9, 2, 8, 4]
filtered_numbers = []

for i in numbers:
    if i > 4:
        filtered_numbers.append(i)

print(filtered_numbers)

# сделал чпек:
# filtered_numbers = [i for i in numbers if i > 4]