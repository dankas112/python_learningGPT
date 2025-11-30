import json
from fuctions_for_library import book_format as bf, books_looks as bl, save_library as sl

LIB_PATH = 'json_learning/ex_1/library.json'
books_in_lib = []

# ====Загружаем библиотеку====
try:
    with open(LIB_PATH, 'r', encoding='utf8') as f:
            books_in_lib = json.load(f)
except FileNotFoundError:
    print('Файл не найден')
except json.JSONDecodeError:
    print('Файл поврежден')

# ====Основная программа====
while True:
    print('\nЭто библиотека книг в формате .json!', 
        '1 - просмотреть список книг', 
        '2 - добавить новую книгу',
        '3 - поиск книг по словарю', 
        '4 - отчистить библиотеку', 
        '5 - удаление выбранной книги', 
        '6 - изменение книги', 
        '0 - выйти', 
        sep='\n')
    
    
    user_input = input('Ожидание ввода: ')
    print('\n')
    # ----Показать книги----
    if user_input == '1':
            bl(books_in_lib)
    # ----Создать новую----
    elif user_input == '2':
        book_name = input('Введите название книги: ')
        book_auth = input('Введите автора книги: ')
        book_year = input('Введите год издания книги: ')
        
        new_book = bf(book_name, book_auth, book_year)
        if new_book is None:
            print('Ошбика данных, книга не добавлена!')
        else:
            books_in_lib.append(new_book)
        
        sl(LIB_PATH, books_in_lib)
        print("Книга добавлена!")
    # ----Поиск книг----
    elif user_input == '3':
        search_key = input('Поиск: ').lower()
        is_found = False
        print('Вот что удалось найти по вашему запросу: ')
        for x in books_in_lib:
            if search_key in x['name'].lower() or search_key in x['author'].lower():
                print(f'"{x["name"]}" - {x["author"]}, {x["year"]}г')
                is_found = True
        if is_found == False:
            print('Ничего не найдено!')
        print('Поиск завершен!\n')
    # ----Удаление содержимого библиотеки----    
    elif user_input == '4':
        delete_lib = input('Чтобы удалить ВСЮ БИБЛИОТЕКУ введите "УДАЛИТЬ"')
        if delete_lib == "УДАЛИТЬ":
            books_in_lib = []
            sl(LIB_PATH, books_in_lib)
            print('Библиотека полностью очищена!')
        else:
            print('Библиотка не тронута!')
            continue
    # ----Удаление отдельной книги----
    elif user_input == '5':
        bl(books_in_lib)
        try:
            book_del_num = int(input('Введите номер книги, которую хотите удалить: '))
            if book_del_num > 0:
                books_in_lib.pop(book_del_num-1)
                sl(LIB_PATH, books_in_lib)
                print('Книга успешно удалена!')
            else:
                print('Такой книги нет!(Введен отрицательный или нулевой номер книги!)')
                                 
        except ValueError:
            print('Ошибка - введено не числовое значение!')
        except IndexError:
            print('Ошибка - такой книги нет!(несуществующий номер книги)')
    
    # ----Изминение книги----
    elif user_input == '6':
        bl(books_in_lib)
        try:
            book_change_num = int(input('Введите номер книги, которую хотите изменить: '))
            if book_change_num > 0:
                print(books_in_lib[book_change_num-1])
                
                changed_name = input('Хотите изменить название?(Enter - пропустить)')
                changed_author = input('Хотите изменить автора?(Enter - пропустить)')
                changed_year = input('Хотите изменить год?(Enter - пропустить)')
                
                if changed_name == '':
                    changed_name = books_in_lib[book_change_num-1]["name"]
                if changed_author == '':
                    changed_author = books_in_lib[book_change_num-1]["author"]
                if changed_year == '':
                    changed_year = books_in_lib[book_change_num-1]["year"]
                    
                changed_book = bf(changed_name, changed_author, changed_year)
                if changed_book is None:
                    print('Ошбика данных, книга не обновлена!')
                else:
                    books_in_lib[book_change_num-1] = changed_book
                    
                sl(LIB_PATH, books_in_lib)
                print(f'Книга {changed_name} обновлена!')
            else:
                print('Такой книги нет!(Введен отрицательный или нулевой номер книги!)')
            
            
        except ValueError:
            print('Ошибка - введено не числовое значение!')
        except IndexError:
            print('Ошибка - такой книги нет!(несуществующий номер книги)')        
            
    # ----Выход----          
    elif user_input == '0':
        print('Выход...\n')
        break        
    # ----Неизвестная команда----
    else:
        print('Неизвестная команда!')