from collections import deque

td = deque([])
created_tasks = 0
completed_tasks = 0
n = 1
print(f'Это симулятр очереди задач!\n Чтобы добавить новую задачу - введите "U"\n Чтобы удалить 1ю в списке задачу - введите "D"\n Чтобы завершить работу - введите "E"')
while True:
    user_task = str(input(f'Что делаем сейчас?: ')).lower()
    if user_task == 'u':
        td.append(n)
        print('Созданна новая задача!')
        n += 1
        created_tasks += 1
    elif user_task == 'd':
        if len(td) != 0:
            td.popleft()
            print('Задача выполнена!')
            completed_tasks += 1
        else: 
            print(f'Нечего удалять!')
    elif user_task == 'e':
        print(f'Задач выполнено: {completed_tasks}, всего задач созданно: {created_tasks}')
        break
    else:
        print('Неверный ввод!')