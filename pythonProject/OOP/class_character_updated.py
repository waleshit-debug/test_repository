class Character:
    def __init__(self, name, damage):
        self.name = name
        self._health = 100
        self._damage = damage

    def take_damage(self, amount):
        self._health -= amount

    def attack(self, target):
        target.take_damage(self._damage)

    def get_status(self):
        return f'Имя: {self.name}, Здоровье: {self._health}'


class Warrior(Character):
    def __init__(self, name, damage, armor):
        self.armor = armor
        super().__init__(name, damage)

    def take_damage(self, amount):
        actual_damage = max(0, amount - self.armor)
        super().take_damage(actual_damage)


class Mage(Character):
    def __init__(self, name, damage, mana):
        self.mana = mana
        super().__init__(name, damage)

    def attack(self, target):
        if self.mana >= 10:
            super().attack(target)
            self.mana -= 10
        else:
            pass


warrior = Warrior("Конан", 15, 5)  # Урон 15, Броня 5
mage = Mage("Раистлин", 20, 100)  # Урон 20, Мана 100

print(warrior.get_status())
print(mage.get_status())
print("--- Битва ---")

# Маг атакует воина
mage.attack(warrior)
print(warrior.get_status())  # Воин должен получить 15 урона (20 - 5 брони)

# Воин атакует мага
warrior.attack(mage)
print(mage.get_status())  # Маг должен получить 15 урона

# Проверка логики мага
mage.mana = 5  # Устанавливаем мало маны
mage.attack(warrior)
print(warrior.get_status())  # Здоровье воина не должно измениться
