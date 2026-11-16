class SpaceShip:
    agency = "Python Space"
    total_ships = 0

    def __init__(self, name: str, max_fuel: int):
        self.name = name
        self.max_fuel = max_fuel
        self.current_fuel = 0
        SpaceShip.total_ships += 1

    def refuel(self, amount: int):
        if self.current_fuel + amount <= self.max_fuel:
            self.current_fuel += amount
            print(f'{self.name}: заправлено {amount} ед. топлива')
        else:
            print(f"{self.name}: топливный бак переполнен")

    def fly(self, fuel_cost: int):
        if self.current_fuel >= fuel_cost:
            self.current_fuel -= fuel_cost
            print(f'{self.name}: полет выполнен, потрачено {fuel_cost} ед. топлива')
        else:
            print(f'{self.name}: недостаточно топлива')

    def show_info(self):
        print(f'Корабль {self.name} | Агентство: {self.agency} | Топливо: {self.current_fuel}/{self.max_fuel}')

    def set_personal_agency(self, agency):
        self.agency = agency


# ----

name_1 = input()
max_fuel_1 = int(input())

name_2 = input()
max_fuel_2 = int(input())

amount_1 = int(input())
amount_2 = int(input())

fuel_cost_1 = int(input())
fuel_cost_2 = int(input())

new_company = input()
personal_company = input()

ship_1 = SpaceShip(name_1, max_fuel_1)
ship_2 = SpaceShip(name_2, max_fuel_2)

ship_1.refuel(amount_1)
ship_2.refuel(amount_2)

SpaceShip.agency = new_company
ship_1.set_personal_agency(personal_company)

ship_1.fly(fuel_cost_1)
ship_2.fly(fuel_cost_2)

ship_1.show_info()
ship_2.show_info()


print(f"Всего кораблей: {SpaceShip.total_ships}")
