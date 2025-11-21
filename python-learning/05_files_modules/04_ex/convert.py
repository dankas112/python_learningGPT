# 4️⃣ Средний уровень — сделай модуль конвертации

# Создай файл convert.py с функциями:

# km_to_miles(km)

# celsius_to_fahrenheit(c)

# seconds_to_hours(sec)

# Импортируй в другом файле и протестируй.

def km_to_miles(km):
    return round(km / 1.609, 2)

def celsius_to_fahrenheit(c):
    return round((c * 9/5) + 32, 1)

def sec_to_hours(sec):
    return round(sec / 3600, 0)