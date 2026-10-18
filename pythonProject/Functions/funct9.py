def fucntion9(day, balance):
    if day > 3 or day < 1 or balance < 30:
        print('Bad')
    else:
        print(function10(day, balance))


def function10(day, balance):
    open('file.txt', 'w').close()
    fee = 7
    count = 1
    while count < day + 1:
        left = balance - fee
        with open('file.txt', 'a') as file:
            file.write(f'{count} день - баланс {balance} - списалось {fee} - осталось {left}\n')
        balance = balance - fee
        count += 1
    with open('file.txt', 'r') as file:
        return file.read()


day = int(input())
balance = int(input())
fucntion9(day, balance)
