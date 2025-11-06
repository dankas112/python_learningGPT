""" Задача 3: Подсчёт гласных и согласных

Пользователь вводит строку

Подсчитать и вывести количество гласных и согласных букв """

user_str = input('Введите строку\слово: ')

let_vowels = 0
let_consonants = 0
vowels = 'AEIOUaeiou'
consonants = 'BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz'

for i in user_str:
    if i in vowels:
        let_vowels += 1
    elif i in consonants:
        let_consonants += 1
        
        
print(f'Количество гласных: {let_vowels}, согласных: {let_consonants}')