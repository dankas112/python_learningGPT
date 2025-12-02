from json import dumps, dump

def book_format(name='book name', 
                author='author of it book', 
                year='year of realise it book'):
    try:
        formated_book = {'name':str(name), 'author':str(author), 'year':int(year)}
    except ValueError:
        print('Невернный тип введенных данных')
        return None
        
    return formated_book


def books_looks(books_lib):
    print('Книги уже лежащие в библиотеке: ')
    n = 0
    for x in books_lib:
        n += 1
        print(f'{n}. "{x["name"]}" - {x["author"]}, {x["year"]}г')
    print()

def save_library(path, books):
    with open(path, 'w', encoding='utf8') as f:
        dump(books, f, ensure_ascii=False, indent=4)