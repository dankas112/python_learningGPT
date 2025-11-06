# 3. Минимум, максимум и среднее

# Функция stats_plus(*args) должна возвращать три значения:
# минимум, максимум и среднее из переданных чисел.
# Пример:

# min_, max_, avg = stats_plus(1, 5, 3, 9)
# print(min_, max_, avg)

def stats_plus(*args):
    return min(args), max(args), sum(args) / len(args)

min_, max_, avg = stats_plus(1, 5, 3, 9)
print(min_, max_, avg)