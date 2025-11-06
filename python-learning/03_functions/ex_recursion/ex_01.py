# Задача 1 (простая):

# Напиши функцию countdown(n),
# которая выводит числа от n до 1, а затем строку "Пуск!", используя рекурсию.
# Пример:

# countdown(3)
# # 3
# # 2
# # 1
# # Пуск!

def countdown(n):
    if n >= 1:
        print(n)
        return countdown(n-1)
    else:
        print('Пуск!')
    
countdown(3)