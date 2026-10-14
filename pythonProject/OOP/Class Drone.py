class DeliveryDrone:
    company = "PythonExpress"
    total_drones = 0

    def __init__(self, name: str, max_weight: int):
        self.name = name
        self.max_weight = max_weight
        self.current_weight = 0
        DeliveryDrone.total_drones += 1

    def load(self, weight):
        actual_weight = self.current_weight + weight
        if actual_weight <= self.max_weight:
            print(f'{self.name}: груз {weight} кг загружен')
            self.current_weight = actual_weight
        else:
            print(f'{self.name}: недостаточно места')

    def deliver(self):
        print(f'{self.name}: доставлено {self.current_weight} кг')
        self.current_weight = 0

    def show_info(self):
        print(f'Дрон {self.name} | Компания: {self.company} | Груз: {self.current_weight}/{self.max_weight} кг')

    def set_personal_company(self, company):
        self.company = company


name_1 = input()
max_weight_1 = int(input())
name_2 = input()
max_weight_2 = int(input())
weight_1 = int(input())
weight_2 = int(input())

new_dd_company_name = input()
company_1 = input()

drone_1 = DeliveryDrone(name_1, max_weight_1)
drone_2 = DeliveryDrone(name_2, max_weight_2)

drone_1.load(weight_1)
drone_2.load(weight_2)

DeliveryDrone.company = new_dd_company_name

drone_1.set_personal_company(company_1)

drone_1.show_info()
drone_2.show_info()
drone_1.deliver()
drone_1.show_info()

print(DeliveryDrone.total_drones)