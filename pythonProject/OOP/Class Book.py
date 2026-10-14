class Book:
    def __init__(self, title: str, author: str, year: int):
        self.is_read = False
        self.status = "Прочитана" if self.is_read else "Не прочитана"
        self.title = title
        self.author = author
        self.year = year

    def read(self):
        self.is_read = True
        print(f'Книга {self.title} прочитана')

    def info(self):
        print(f'{self.author}: {self.title} ({self.year}) — {self.status}')


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_all(self):
        for f in self.books:
            f.info()

    def find_by_author(self, search: str):
        for f in self.books:
            if search == f.author:
                f.info()
            else:
                print(f'Книг автора {search} не найдено.')


# Тестовые данные
# Создаем книги
book1 = Book("Война и мир", "Лев Толстой", 1869)
book2 = Book("Преступление и наказание", "Федор Достоевский", 1866)
book3 = Book("Анна Каренина", "Лев Толстой", 1877)

# Создаем библиотеку
my_library = Library()

# Добавляем книги
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

# Выводим все книги
print("--- Все книги ---")
my_library.show_all()

# Читаем одну книгу
print("\n--- Читаем книгу ---")
book1.read()

# Ищем книги Толстого
print("\n--- Книги Толстого ---")
my_library.find_by_author("Лев Толстой")

# Ищем книги неизвестного автора
print("\n--- Книги неизвестного автора ---")
my_library.find_by_author("Пушкин")
