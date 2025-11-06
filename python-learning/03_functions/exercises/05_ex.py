# Задача 5. Проверка на простое число

# Создай функцию is_prime(num), которая возвращает:

# True, если число простое;

# False — если нет.
# (Простое — делится только на 1 и само себя)


def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

print(is_prime(2))
print(is_prime(13))
print(is_prime(17))
print(is_prime(7))

print(is_prime(64))
print(is_prime(4))
print(is_prime(25))
print(is_prime(100))