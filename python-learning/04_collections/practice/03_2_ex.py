from collections import defaultdict
user_dict = defaultdict(list)

while True:
    user_input = str(input("Введите пару вида: 'имя предмета'-'пробел'-'оценка': "))
    user_list = user_input.split()
    if user_input == "стоп":
        break
    elif len(user_list) != 2:
        print('Некоректный ввод! Попробуйте еще раз!')
    else:
        user_dict[user_list[0]] += [int(user_list[1])]
        print('Оценка добавлена!')

for subject, marks in user_dict.items():
    avg = sum(marks) / len(marks)
    print(f'По предмету: {subject} оценки: {marks} средний бал - {avg:.2f}')