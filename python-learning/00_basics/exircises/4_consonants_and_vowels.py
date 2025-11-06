""" Напиши программу, которая:
Принимает строку от пользователя
Считает количество гласных и согласных в строке
    Пример:
Введите строку: Hello World
Гласных: 3
Согласных: 7 """

consonants = 'bcdfghjklmnpqrstvwx'
vowels = 'aeiouy'
res_c = 0
res_v = 0
user_word = input('Введите строку: ')
for x in user_word:
    if x.lower() in consonants:
        res_c += 1
    elif x.lower() in vowels:
        res_v += 1
print(f"Согласных: {res_c}\nГласных: {res_v}" )