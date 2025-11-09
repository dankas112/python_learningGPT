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