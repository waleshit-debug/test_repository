class Account:
    def __init__(self, account_number: str, balance: float):
        self.amount = None
        self.account_number = account_number
        self.balance = balance

    # пополнение баланса
    def deposit(self, amount):
        self.amount = amount
        self.balance += amount
        print(f'Счет {self.account_number}: зачислено {self.amount}. Текущий баланс: {self.balance}')

    def withdraw(self, amount):
        self.amount = amount
        if self.balance >= amount:
            self.balance -= amount
            print(f'Счет {self.account_number}: снято {self.amount}. Остаток: {self.balance}')
        else:
            print(f'Недостаточно средств на счете {self.account_number}')

    def get_balance(self):
        return self.balance


class SavingAccount:
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate # как перевести в процент?
        self.comission = self.amount * 0.01

    def withdraw(self, amount):
        if self.balance >= amount + self.comission:
            self.balance -= amount
            print(f'Счет {self.account_number}: снято {self.amount}. Комиссия за операцию составила {self.comission}.'
                  f' Остаток: {self.balance}')
        else:
            print(f'Недостаточно средств на счете {self.account_number}')

    

