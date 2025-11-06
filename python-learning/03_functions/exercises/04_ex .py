# Задача 4. Факториал числа

# Напиши функцию factorial(n), которая возвращает факториал числа n (например, 5! = 120).
# Не используй math.factorial.

def factorial(n):
    result = 1
    for x in range(1, n+1):
        result = result * x
    return result

print(factorial(3))
print(factorial(5))
print(factorial(6))
print(factorial(1))
