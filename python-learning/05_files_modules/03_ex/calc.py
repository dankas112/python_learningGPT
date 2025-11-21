# 3️⃣ Используй __name__ == "__main__"

# Создай файл calc.py:

# В нём:

# функция add(a, b)

# функция sub(a, b)

# блок:

# if __name__ == "__main__":
#     print(add(2, 3))
#     print(sub(5, 1))


# Затем создай другой файл run.py, импортируй только функцию add и вызови её.

# Проверь, что тесты внутри calc.py не запускаются при импорте.

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

if __name__ == "__main__":
    print(add(2, 3))
    print(sub(5, 1))
    
