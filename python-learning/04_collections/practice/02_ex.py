# 2. deque

# Задача:
# Смоделируй очередь задач.

# Пользователь может добавлять задачи (append) и выполнять их (popleft).

# Когда пользователь вводит done, программа завершает работу и показывает, сколько задач было выполнено.
from collections import deque


td = deque([])
n = 1
print(len(td))
print(f'Это симулятр очереди задач!\n Чтобы добавить новую задачу - введите "U"\n Чтобы удалить 1ю в списке задачу - введите "D"\n Чтобы завершить работу - введите "E"')
while True:
    user_task = str(input(f'Что делаем сейчас?: ')).lower()
    if user_task == 'u':
        td.append(n)
        print('Созданна новая задача!')
        n += 1
        print(n)
    elif user_task == 'd':
        if len(td) != 0:
            td.popleft()
            print('Задача удалена!')
        else: 
            print(f'Нечего удалять!')
    elif user_task == 'e':
        print(f'Задач выполнено: {td[0]}, всего задач созданно: {td[-1]}')
        break
    else:
        print('Неверный ввод!')
        
# Ошибка:

# td[0] и td[-1] — это id задач, а не количество.

# Если очередь пустая — произойдёт ошибка доступа по индексу.

# ✔ Как правильно:

# Хранить только количество выполненных задач:

# from collections import deque

# td = deque()
# created = 0
# done = 0

# print(f'Это симулятор очереди задач!")
# print("U — создать задачу\nD — выполнить\nE — выход")

# while True:
#     cmd = input("Что делаем?: ").lower()

#     if cmd == 'u':
#         created += 1
#         td.append(created)
#         print("Создана новая задача!")

#     elif cmd == 'd':
#         if td:
#             td.popleft()
#             done += 1
#             print("Задача выполнена!")
#         else:
#             print("Очередь пуста!")

#     elif cmd == 'e':
#         print(f"Создано задач: {created}")
#         print(f"Выполнено задач: {done}")
#         print(f"Осталось в очереди: {len(td)}")
#         break

#     else:
#         print("Неверный ввод!")


# Теперь всё корректно работает.