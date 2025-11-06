# Задача 4: Список чисел

# Пользователь вводит 5 чисел через пробел

# Программа создаёт список этих чисел

# Вывести: сумму, среднее, минимальное и максимальное число

import sys
user_numbers = str(input('Введите 5 чисел через пробел: '))


result_numbers = user_numbers.split()
result_sum = 0
num_list = []

if len(result_numbers) != 5:
    print("Чет ты много ввел!")
    sys.exit()

for i in result_numbers:
    result_sum += int(i)
    num_list.append(int(i))

num_list.sort()

print(f'Сумма введеных чисел: {result_sum}, среднее число: {result_sum//5}, максимальное число: {num_list[-1]}, минимальное число: {num_list[0]}.')

# сделал чпек:
# nums = list(map(int, input('Введите 5 чисел через пробел: ').split()))
# if len(nums) != 5:
#     print("Нужно ровно 5 чисел!")
# else:
#     print(f"Сумма: {sum(nums)}, Среднее: {sum(nums)/5}, Макс: {max(nums)}, Мин: {min(nums)}")