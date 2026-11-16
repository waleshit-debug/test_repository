class LibraryBook:
    library_name = 'PythonLibrary'
    total_books = 0

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.is_available = True
        self.reader = 'Нет'

        LibraryBook.total_books += 1

    def borrow(self, reader):
        if self.is_available:
            self.is_available = False
            self.reader = reader
            print(f'{self.title}: книга выдана читателю {self.reader}')
        else:
            print(f'{self.title}: книга уже выдана')

    def return_book(self):
        if self.is_available:
            print(f'{self.title}: книга уже находится в библиотеке')
        else:
            print(f'{self.title}: книга возвращена читателем {self.reader}')
            self.is_available = True
            self.reader = 'Нет'

    def show_info(self):
        if self.is_available:
            print(f'Книга "{self.title}" | Автор: {self.author} | Библиотека: {self.library_name} | Статус: доступна')
        else:
            print(f'Книга "{self.title}" | Автор: {self.author} | Библиотека: {self.library_name} | Статус: выдана '
                  f'читателю {self.reader}')

    def set_personal_library(self, library_name):
        self.library_name = library_name


title_1 = input()
author_1 = input()

title_2 = input()
author_2 = input()

reader_1 = input()
reader_2 = input()

new_library_name = input()
personal_library_name = input()

book_1 = LibraryBook(title_1, author_1)
book_2 = LibraryBook(title_2, author_2)

book_1.borrow(reader_1)
book_2.borrow(reader_2)
book_2.borrow(reader_1)


LibraryBook.library_name = new_library_name
book_1.library_name = personal_library_name

book_1.return_book()

book_1.show_info()
book_2.show_info()


print(f"Всего книг: {LibraryBook.total_books}")
