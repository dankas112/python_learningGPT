# 3. defaultdict

# Задача:
# Пользователь вводит пары вида "имя предмета оценка" (например: Математика 5, Физика 4, Математика 3)
# Создай словарь, где ключ — предмет, а значение — список оценок.
# После ввода стоп — выведи средний балл по каждому предмету.

from collections import defaultdict
user_dict = defaultdict(str)

while True:
    user_input = str(input("Введите пару вида: 'имя предмета'-'пробел'-'оценка': "))
    user_list = user_input.split()
    if user_input == "стоп":
        break
    elif len(user_list) != 2:
        print('Некоректный ввод! Попробуйте еще раз!')
    else:
        user_dict[user_list[0]] += user_list[1] + ' '
        print('Оценка добавлена!')

print(f'Вот список оценок: {user_dict}')

# defaultdict — Работает, но тип данных выбран неверно

# Ты сделал:

# user_dict = defaultdict(str)


# И потом добавляешь строки:

# user_dict[user_list[0]] += user_list[1] + ' '

# ❗ Минус:

# Сложно потом считать средний балл.

# Хранить оценки строкой — плохая практика.

# ✔ Как правильно:

# Использовать список:

# user_dict = defaultdict(list)

# while True:
#     user_input = input("Введите предмет и оценку: ")
#     if user_input == "стоп":
#         break

#     parts = user_input.split()
#     if len(parts) != 2:
#         print("Некорректный ввод!")
#         continue

#     subject, mark = parts
#     user_dict[subject].append(int(mark))


# И затем:

# for subject, marks in user_dict.items():
#     avg = sum(marks) / len(marks)
#     print(f"{subject}: {avg:.2f}")