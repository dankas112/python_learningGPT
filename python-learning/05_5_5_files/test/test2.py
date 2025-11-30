from colorama import Fore, Style
from random import randint
from time import sleep, localtime

g = Fore.GREEN
y = Fore.YELLOW
r = Fore.RED
b = Fore.BLACK
c = Fore.CYAN
m = Fore.MAGENTA
tl = localtime()

def weekday_abc(weekday):
    week_abc = ('Понедельник', 'Вторник',
                'Среда', 'Четверг',
                'Пятница', 'Суббота', 'Воскресенье')
    return week_abc[weekday]

print(y + f'Время сейчас: {tl[3]}ч {tl[4]}м')

while True: # добавить дату время
    print(g + '|СПИСОК ДОСТУПНЫХ КОМАНД:' , 
        m + '|[w] - добавить строку со своим текстом|', 
        '|[r] - зачитать выбираемую строку|', 
        '|[g] - сгенрировать число|', 
        '|[d] - какой сейчас день?', 
        '|[e] - выход|',  sep='\n')
    user_in = input(c + 'Ожидается ввод: ')
    
    if user_in.lower() == 'w':
        print(g + 'Режим: запись')
        with open('test2.txt', mode='a', encoding='utf-8') as f:
            writing_text = input(c + 'Что напишем?: ') + '\n'
            f.write(writing_text)
            
    elif user_in.lower() == 'r':
        print(g + 'Режим: чтение')
        try:
            with open('test2.txt', mode='r', encoding='utf-8') as f:
                lines_in_file = f.readlines()
                print(f'Всего строк в файле на данный момент: {len(lines_in_file)}')
                line_num = input(c + 'Какую прочитать?:')
                print((lines_in_file[line_num - 1])[:-1])
                
        except TypeError:
            print(r + 'Неверное значение строки!') #сделать по классам и быстрое написание
        except IndexError:
            print(r + 'Такой строки не существует!')
        except ValueError:
            print(r + 'Введено не численное значение!')
            
    elif user_in.lower() == 'g':
        try:
            print('Режим: генерация чисел')
            user_random_num = input('Введите диапозон через пробел: от(число)-пробел-до(число)').split()
            for x in range(3):
                print('Бросаем кубик') #сделать чтобы точки типа \. \.. \... возможно сделать функцию задержки и понадобвлять везде
                
                sleep(1)
            print(randint(int(user_random_num[0]), int(user_random_num[1])))
            
        except TypeError:
            print(r + 'Неверное значение строки!')
        except IndexError:
            print(r + 'Такой строки не существует!')
        except ValueError:
            print(r + 'Введено не численное значение или не по формату!')
            
    elif user_in.lower() == 'd':
        print(y + f'Сегодня {tl[2]}/{tl[1]}/{tl[0]}, ', end='')
        print(f'день недели - {weekday_abc(tl[-3])}')
        
    elif user_in.lower() == 'e':
        print(g + 'ВЫХОД', Style.RESET_ALL)
        break
    
    else:
        print(r + 'Команда введена неверно, отсутсвует или возможно вы ввели лишние знаки')
