# Задача 2 (средняя):

# Напиши рекурсивную функцию sum_list(numbers),
# которая возвращает сумму всех элементов списка.
# Нельзя использовать sum(), циклы for или while.

# Пример:

# sum_list([1, 2, 3, 4])  # 10
# sum_list([])             # 0

def sum_list(user_list):
    if len(user_list) == 1:
        return user_list[0]
    elif len(user_list) < 1:
        return 0
    else:
       return user_list[0] + sum_list(user_list[1:])
print(sum_list([1, 2, 3, 4]))  # 10
print(sum_list([]))            # 0