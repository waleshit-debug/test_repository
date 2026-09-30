class Feline:
    """модель кота"""

    def __init__(self, name: str, age: int, color: str, breed: str):
        """инициализация атрибутов кота: возраст и окрас"""
        self.name = name
        self.age = age
        self.color = color
        self.breed = breed
        print('Кот создан')

    def meow(self):
        print(self.name + 'орет')

    def run(self):
        print(self.name + 'бежит орет')

    def description(self):
        description = f'Кота зовут {self.name}, коту {self.age} лет, окрас - {self.color}. Порода кота - {self.breed}'
        return description

    def count_letter(self):
        """Получение количества букв в алфавите"""
        count = (len(self.name))
        print(f"Количество букв в коте равно: {count}")


koshka = Feline('Кошка', '5', 'табби', 'метис')
print(koshka.description())

class Domesticated(Feline):
    """create 'domesticated cat' class"""

    def __init__(self, name, age, color, breed):
        super().__init__(name, age, color, breed)

    # здесь можно задать параметры по умолчанию и переопределить значения по умолчанию из родительского класса.
    # Через метод init мы получаем информацию, которая необходима для создания экземпляра класса Feline.
    # Все атрибуты родительского класса таким образом передаются в подкласс

    # '''через функцию super обозначается связь родительского класс с подклассом.
    # В этой строке __init__ подкласса связывается с __init__ родителя, благодаря чему потомок получает все
    # атрибуты родительского класса и их не нужно еще раз прописывать вручную'''

    def get_weakness(self):
        print(f'У животного есть риски заболевания следующих органов: {self.weakness}')

# этот метод доступен только для экземпляров класса потомка


myakish = Domesticated('Мякиш', '5', 'табби', 'красотуля')
print(myakish.description())
myakish.update_age(5)
print(myakish.description())
myakish.get_weakness()

