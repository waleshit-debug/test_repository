# Класс (Шаблон/Тип данных)
class User:
    pass


# Объекты (Конкретные данные в памяти)
user1 = User()
user2 = User()

# Класс: User
# Процесс: User() (вызов класса как функции запускает «сборку» объекта).
# Объект (Экземпляр): user_alex (переменная, в которой хранится результат).
user_alex = User()


class Cat:
    # Конструктор, который создает атрибуты
    def __init__(self, name: str, satiety: int):
        # Этот код выполнится АВТОМАТИЧЕСКИ в момент создания объекта
        self.name = name
        self.satiety = 5  # Начальное состояние сытости
        print(f"Кота по имени {name} создали!")

    # Метод
    @staticmethod
    def cat_meow():
        print("Ха-ха, то есть мяу")

    # Метод, который ЧИТАЕТ атрибуты
    def cat_show_status(self):
        print(f"Имя: {self.name}, Сытость: {self.satiety}")

    # Метод, который ИЗМЕНЯЕТ атрибут
    def cat_eat(self, food: int):
        print(f"{self.name} ест...")
        # Мы используем self, чтобы получить доступ к АТРИБУТУ этого же объекта
        self.satiety = self.satiety + food
        # self.satiety = self.satiety + 3 значит то же что и "barsik.satiety = barsik.satiety + 3".
        print(f"Сытость увеличилась!")


barsik = Cat("Барсик", 4)
# или
marsik = Cat()
marsik.name = "Марсик"
marsik.satiety = 4

marsik.cat_eat(2)
# то же что и Cat.cat_eat(marsik, 2). Чтобы два раза не писать marsik, в определении метода cat_eat используется self 


barsik.cat_show_status()
# возвращает "Имя: barsik, Сытость: 5")
