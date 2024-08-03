import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    text1=text[start:start+size]
    #print(text1)
    if text1[-1] in (",", ".", "!", ":", ";", "?") and text1[-2] not in (",", ".", "!", ":", ";", "?"):
        return [text1, len(text1)]
    else:
        for i in text1[-2::-1]:
            ind=text1[::-1].index(i)
            if i in (",", ".", "!", ":", ";", "?") and text1[-ind-2] not in (",", ".", "!", ":", ";", "?") and text1[-ind] not in (",", ".", "!", ":", ";", "?"):
               
                return [text1[:-ind], len(text1[:-ind])]
            
    pass

# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    start = 0
    page_number = 1
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
    while start < len(text):
        page_text, length = _get_part_text(text, start, PAGE_SIZE)
        if page_text:
            book[page_number] = page_text.lstrip()
            page_number += 1
            start += length
        else:
            break
    pass
print(book)
# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(BOOK_PATH)
print(book)