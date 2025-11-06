# Задача 2. Возведение в степень (рекурсивно)

# Напиши функцию power(base, exp),
# которая вычисляет base в степени exp с помощью рекурсии.
# (не используя ** и pow())

# Примеры:

# power(2, 3) → 8
# power(5, 0) → 1
# power(3, 2) → 9

def power(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return power(base, exp-1) * base
    
print(power(2, 3))
print(power(5, 0))
print(power(3, 2))

# Можно даже упростить, ведь elif exp == 1 необязателен:

# def power(base, exp):
#     if exp == 0:
#         return 1
#     return base * power(base, exp - 1)