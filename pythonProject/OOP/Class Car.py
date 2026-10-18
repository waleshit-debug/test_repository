class Car:
    def __init__(self, model, year, engine_capacity, price, mileage, wheels):
        self.model = model
        self.year = year
        self.engine_capacity = engine_capacity
        self.price = price
        self.mileage = mileage
        self.wheels = 4

    def get_info(self):
        get_info = (
            f'Это - автомобиль модели {self.model} {self.year} года выпуска с объемом двигателя {self.engine_capacity} литров. '
            f'У машины есть колеса - {self.wheels} шт. '
            f'Купить такую машину с пробегом {self.mileage} км можно за {self.price} рублей')

        return get_info


lada = Car('Lada Granta', 2024, 1.6, 980000, 60, 4)
print(lada.get_info())


class Truck(Car):

    def __init__(self, model, year, engine_capacity, price, mileage, wheels):
        super().__init__(model, year, engine_capacity, price, mileage, wheels)
        self.wheels = 8


kamaz = Truck('КамАЗ 5490', 2015, 12, 1750000, 120, 8)
print(kamaz.get_info())
