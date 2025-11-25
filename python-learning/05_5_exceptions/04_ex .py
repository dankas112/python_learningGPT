# 4) Преобразование строки в число (средняя)

# Функция to_int(s):

# возвращает int(s)

# но если преобразовать нельзя — возвращает 0

# если s = None → вернуть -1

# Примеры:

# to_int("123") → 123
# to_int("abc") → 0
# to_int(None) → -1

def to_int(s):
    try:
        s = int(s)
    except(ValueError):
        return 0
    except(TypeError):
        return -1
    else:
        return s
    
print(to_int("123"))
print(to_int("abc"))
print(to_int(None))