# Справочник пользователя

# Напиши функцию user_info(**kwargs),
# которая принимает любое количество именованных аргументов
# и выводит их в виде:

# ключ: значение


# Пример:

# user_info(name='Антон', age=25, hobby='программирование')

def user_info(**kwargs):
    user_list = list(kwargs.keys())
    for x in range(len(kwargs)):
        print(f'{user_list[x]} : {kwargs[user_list[x]]}')
    
user_info(name='Антон', age=25, hobby='программирование')

# правки:
# for key, value in kwargs.items():
#     print(f"{key}: {value}")