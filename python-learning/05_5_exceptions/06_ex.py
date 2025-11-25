# 6) Многоуровневое исключение (сложная)

# Напиши функцию process(data):

# Пытается взять data["value"]

# Преобразует его в int

# Делит 100 на полученное число

# Возвращает результат

# Ловить ошибки:

# Нет ключа "value" → вернуть "Нет ключа"

# Невозможно преобразовать в число → "Неверный формат"

# Деление на ноль → "Деление на ноль"

# Примеры:

# process({"value": "20"}) → 5
# process({}) → "Нет ключа"
# process({"value": "abc"}) → "Неверный формат"
# process({"value": "0"}) → "Деление на ноль"

def process(data):
    try:
        result = 100/int(data['value'])
    except(ValueError):
        print('Неверный формат')
    except(ZeroDivisionError):
        print('Деление на ноль')
    except(KeyError):
        print('Нет ключа')
    else:
        print(result)
        return result

process({"value": "20"})
process({})
process({"value": "abc"})
process({"value": "0"})

