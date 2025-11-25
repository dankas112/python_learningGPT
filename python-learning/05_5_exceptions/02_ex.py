# 2) Сумма списка с проверкой (лёгкая)

# Напиши функцию sum_list(lst), которая:

# принимает список

# возвращает сумму элементов

# если в списке есть не числа, функция должна ловить исключение и возвращать строку "Некорректные данные"

# Пример:

# sum_list([1, 2, 3]) → 6
# sum_list([1, "x", 3]) → "Некорректные данные"

def sum_list(lst):
    try:
        if not all(isinstance(x, int) for x in lst):
            raise ValueError('Некорректные данные')
    except(ValueError) as e:
        print(e)
    else:
        print(sum(lst[:]))


sum_list([1, 2, 3])
sum_list([1, "x", 3])