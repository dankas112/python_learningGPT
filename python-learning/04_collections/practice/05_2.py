from collections import OrderedDict
groceries_dict = OrderedDict()

while True:
    user_input = str(input("Введите пару вида: 'товар'-'пробел'-'количество': "))
    user_list = user_input.split()
    if user_input == "стоп":
        break
    elif len(user_list) != 2:
        print('Некоректный ввод! Попробуйте еще раз!')
    else:
        groceries_dict[user_list[0]] = groceries_dict.get(user_list[0], 0) + int(user_list[1])
        print('Товар добавлен!')

for x in groceries_dict.keys():
    print(f'{x} : {groceries_dict[x]}')