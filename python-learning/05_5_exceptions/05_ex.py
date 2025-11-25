# 5) Кастомное исключение (сложная)

# Создай класс исключения NegativeNumberError.

# Функция check_positive(x) должна:

# выбрасывать NegativeNumberError, если x < 0

# возвращать "OK", если число нормальное

# ловить ошибку внутри самой функции и вместо падения возвращать строку "Ошибка: отрицательное число"

# Пример:

# check_positive(5) → "OK"
# check_positive(-3) → "Ошибка: отрицательное число"

class NegativeNumber(ValueError):
    pass

def check_positive(x):
    try:
        if x < 0:
            raise NegativeNumber('Отрицательное число не пройдет')
    except(NegativeNumber) as e:
        print(f'Ошибка - {e}')
    else:
        print('OK')


check_positive(-12)
check_positive(10)



