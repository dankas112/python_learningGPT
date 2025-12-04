from json import dump, load, JSONDecodeError

# 0====Загрузка библиотеки====
def library_load(LIB_PATH):
    try:
        with open(LIB_PATH, 'r', encoding='utf8') as f:
                loaded_lib = load(f)
    except FileNotFoundError:
        print('Файл не найден')
    except JSONDecodeError:
        print('Файл поврежден')
    return loaded_lib

# 1====Принимает список из книг и возвращает строку для вывода====
def books_looks(books_lib):
    will_printed = ['Книги уже лежащие в библиотеке: ']
    n = 0
    for x in books_lib:
        n += 1
        book_in = (f'{n}. "{x["name"]}" - {x["author"]}, {x["year"]}г')
        will_printed.append(book_in)
    return will_printed

# 3====Поиск по словарю====
def search(search_key, library):
    searched_values = []
    for x in library:
        if search_key in x['name'].lower() or search_key in x['author'].lower():
            founded_value = (f'"{x["name"]}" - {x["author"]}, {x["year"]}г')
            searched_values.append(founded_value)
    return searched_values

# 4====Удаление всей библиотеки====
def delete_lib(is_delete, LIB_PATH):
    if is_delete == True:
            deleted_lib = []
            save_library(LIB_PATH, deleted_lib)

# ====Сохранение словаря====
def save_library(path, books):
    with open(path, 'w', encoding='utf8') as f:
        dump(books, f, ensure_ascii=False, indent=4)
        
# ====Функция принимает 3 значения и преобразует в словри====
def book_format(name='book name', 
                author='author of it book', 
                year='year of realise it book'):
    try:
        formated_book = {'name':str(name), 'author':str(author), 'year':int(year)}
    except ValueError:
        print('Невернный тип введенных данных')
        return None
    return formated_book

# 5====Удаление отдельной книги====
def book_delete(book_del_num, is_delete, library_main, LIB_PATH):
    try:
        if book_del_num > 0:
            library_main.pop(book_del_num-1)
            save_library(LIB_PATH, library_main)
            return('Книга успешно удалена!')
        else:
            return('Такой книги нет!(Введен отрицательный или нулевой номер книги!)')
                            
    except ValueError:
        print('Ошибка - введено не числовое значение!')
    except IndexError:
        print('Ошибка - такой книги нет!(несуществующий номер книги)')