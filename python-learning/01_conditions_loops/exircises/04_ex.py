""" Задача 4: Сумма чисел

Пользователь вводит числа до тех пор, пока не введёт 0.
Найди их сумму.

Подсказка: while True: и break пригодятся. """


result = 0
while True:
    num = int(input('Введите число!'))
    if num != 0:
        result += num
        print('еще! еще!')
        continue
    else:
        print(f'Сумма всех введеных чисел равна: {result}')
        break
        
    