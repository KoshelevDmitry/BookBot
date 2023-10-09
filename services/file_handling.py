import os
import sys

BOOK_PATH: str = 'book/book.txt'
PAGE_SIZE: int = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    slice = text[start: start + size + 1]
    list = []

    for g in range(3):
        if (start + size) >= len(text) or slice[len(slice)-1] == ' ':
            break
        elif slice[len(slice)-1] in [',', '.', '!', ':', ';', '?']:
            slice = slice[0: len(slice) - 1]
        else:
            break

    for i in [',', '.', '!', ':', ';', '?']:
        list.append(slice.rfind(i)+1)
    slice_new = text[start: start + max(list)]

    return slice_new, max(list)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    file = open(path, encoding='utf-8')
    text = file.read()
    begin_position = 0
    key = 1
    while len(text) - begin_position > 0:
        element_dict = _get_part_text(text, begin_position, PAGE_SIZE)
        book[key] = element_dict[0].lstrip()
        print(key, book[key])
        key += 1

        begin_position = begin_position + element_dict[1]


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
