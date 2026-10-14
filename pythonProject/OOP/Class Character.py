class Character:
    def __init__(self, name: str):
        self.name = name
        self.health = 100
        self.level = 1
        self.damage = 10

    def attack(self):
        print(f'{self.name}  наносит удар!')
        return self.damage

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f'{self.name} повержен!')

    def info(self):
        print(f'{self.name} | Уровень: {self.level} | Здоровье: {self.health}')


class Warrior(Character):
    def __init__(self, name, strength: int):
        super().__init__(name)
        self.strength = strength

    def attack(self):
        print(f'{self.name} бьет мечом!')
        self.damage = self.strength + 10
        return self.damage


class Mage(Character):
    def __init__(self, name, mana: int):
        super().__init__(name)
        self.mana = mana

    def attack(self):
        print(f'{self.name} кастует заклинание!')
        self.damage = 15
        return self.damage

    def cast_heal(self):
        if self.health >= 100:
            print(f'{self.name} уже полностью здоров')
        else:
            self.health = min(100, self.health + 20)
            # Сравнивает 100 и текущее ХП+20, возвращает наименьшее из двух чисел
            print(f'{self.name} восстанавливает 20 HP')


class Arena:
    def __init__(self):
        self.fighters = []

    def add_fighter(self, character):
        self.fighters.append(character)

    def show_all(self):
        for f in self.fighters:
            f.info()

    def battle(self, fighter_1, fighter_2):
        if fighter_1 not in self.fighters or fighter_2 not in self.fighters:
            print(f'Не хватает бойца!')
            return
        fighter_1.attack()
        fighter_2.take_damage(fighter_1.damage)
        if fighter_2.health > 0:
            fighter_2.attack()
            fighter_1.take_damage(fighter_2.damage)
            if fighter_1.health > 0 and fighter_2.health > 0:
                print('Ничья! Оба бойца выжили.')


# Создаем персонажей
warrior = Warrior("Конан", strength=15)
mage = Mage("Мерлин", mana=50)
warrior2 = Warrior("Рэмбо", strength=5)

# Создаем арену
arena = Arena()
arena.add_fighter(warrior)
arena.add_fighter(mage)
arena.add_fighter(warrior2)

# Показываем всех
print("--- Все бойцы ---")
arena.show_all()

# Битва
print("\n--- Битва: Конан vs Мерлин ---")
arena.battle(mage, warrior)

# Лечение мага
print("\n--- Лечение ---")
mage.cast_heal()
mage.cast_heal()

# Итог
print("\n--- Состояние после боя ---")
arena.show_all()
