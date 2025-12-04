import json
from utils import book_format, books_looks, save_library, library_load, search, delete_lib, book_delete
# from storage import

LIB_PATH = 'json_learning/library_defs/data/library.json'
library_main = []

# ====Загружаем библиотеку====

library_main = library_load(LIB_PATH)

# ====Основная программа====

while True:
    # ----Главное меню----
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
    
    # ----Показать книги----
    if user_input == '1':
            books_now = books_looks(library_main)
            for x in books_now:
                print(x)
            
    # ----Создать новую----
    elif user_input == '2':
        book_name = input('Введите название книги: ')
        book_auth = input('Введите автора книги: ')
        book_year = input('Введите год издания книги: ')
        
        new_book = book_format(book_name, book_auth, book_year)
        if new_book is None:
            print('Ошбика данных, книга не добавлена!')
        else:
            library_main.append(new_book)
        
        save_library(LIB_PATH, library_main)
        print("Книга добавлена!")
        
    # ----Поиск книг----
    elif user_input == '3':
        search_key = input('Поиск: ').lower()
        print('Вот что удалось найти по вашему запросу: ')
        searched_values = search(search_key, library_main)
        if len(searched_values) == 0:
            print('Ничего не найдено!')
        else:
            for x in searched_values:
                print(x)
        print('Поиск завершен!\n')
        
    # ----Удаление содержимого библиотеки----    
    elif user_input == '4':
        is_delete = input('Чтобы удалить ВСЮ БИБЛИОТЕКУ введите "УДАЛИТЬ"')
        if is_delete == "УДАЛИТЬ":
            delete_lib(True, LIB_PATH)
            print('Библиотека полностью очищена!')
        else:
            print('Библиотка не тронута!')
        
    # ----Удаление отдельной книги----
    elif user_input == '5':
        books_now = books_looks(library_main)
        for x in books_now:
            print(x)
            
        book_del_num = int(input('Введите номер книги, которую хотите удалить: '))
        print(f'Вы точно хотите удалить: {books_now[book_del_num]}?')
        is_del_book = False
        if input('ЧТобы подтвердить удаление введите "УДАЛИТЬ": ') == 'УДАЛИТЬ':
            is_del_book = True
        print(book_delete(book_del_num, is_del_book, library_main, LIB_PATH))
        
    
    # ----Изминение книги----
    elif user_input == '6':
        books_now = books_looks(library_main)
        for x in books_now:
            print(x)
        try:
            book_change_num = int(input('Введите номер книги, которую хотите изменить: '))
            if book_change_num > 0:
                print(library_main[book_change_num-1])
                
                changed_name = input('Хотите изменить название?(Enter - пропустить)')
                changed_author = input('Хотите изменить автора?(Enter - пропустить)')
                changed_year = input('Хотите изменить год?(Enter - пропустить)')
                
                if changed_name == '':
                    changed_name = library_main[book_change_num-1]["name"]
                if changed_author == '':
                    changed_author = library_main[book_change_num-1]["author"]
                if changed_year == '':
                    changed_year = library_main[book_change_num-1]["year"]
                    
                changed_book = book_format(changed_name, changed_author, changed_year)
                if changed_book is None:
                    print('Ошбика данных, книга не обновлена!')
                else:
                    library_main[book_change_num-1] = changed_book
                    
                save_library(LIB_PATH, library_main)
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