class SecureWallet:
    def __init__(self, owner, balance, pin=0):
        self.owner = owner
        self._balance = balance
        self.__pin = 0

        self.set_balance(self._balance)
        self.set_pin(pin)

    def get_balance(self):
        return self._balance

    def set_balance(self, new_balance):
        if not isinstance(new_balance, int):
            print("Ошибка: баланс должен быть целым числом")
            return
        elif new_balance < 0:
            print('Ошибка: баланс не может быть отрицательным')
        else:
            self._balance = new_balance
            print(f'Баланс установлен: {self._balance}')

    def set_pin(self, new_pin):
        if not isinstance(new_pin, int):
            print('Ошибка: PIN-код должен быть целым числом')
        elif not 1000 <= new_pin <= 9999:
            print('Ошибка: PIN-код должен состоять из 4 цифр')
        else:
            self.__pin = new_pin
            print('PIN-код установлен')

    def __check_pin(self, pin):
        return pin == self.__pin

    def deposit(self, amount):
        if not isinstance(amount, int):
            print('Ошибка: сумма пополнения должна быть целым числом')
        elif amount <= 0:
            print('Ошибка: сумма пополнения должна быть положительной')
        else:
            self._balance += amount
            print(f'Кошелек пополнен на {amount}. Баланс: {self._balance}')

    def withdraw(self, amount, pin):
        if not self.__check_pin(pin):
            print('Ошибка: неверный PIN-код')
        elif not isinstance(amount, int):
            print('Ошибка: сумма снятия должна быть целым числом')
        elif amount < 0:
            print('Ошибка: сумма снятия должна быть положительной')
        elif amount > self._balance:
            print('Ошибка: недостаточно средств')
        else:
            self._balance -= amount
            print(f'Снято {amount}. Баланс: {self._balance}')

    def change_pin(self, old_pin, new_pin):
        if not self.__check_pin(old_pin):
            print('Ошибка: неверный текущий PIN-код')
        else:
            self.set_pin(new_pin)

    def show_info(self):
        print(f'Владелец: {self.owner} | Баланс: {self.get_balance()}')


owner_1 = input()
balance_1 = int(input())
old_pin = int(input())
amount_1 = int(input())
amount_2 = int(input())
confirm_pin = int(input())
new_pin_1 = int(input())

my_wallet = SecureWallet(owner_1, balance_1, old_pin)
my_wallet.deposit(amount_1)
my_wallet.withdraw(amount_2, confirm_pin)
my_wallet.change_pin(confirm_pin, new_pin_1)
my_wallet.withdraw(1, new_pin_1)
my_wallet.set_balance(-100)
my_wallet.set_balance('string')
my_wallet.show_info()

