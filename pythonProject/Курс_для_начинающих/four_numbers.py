print(1624 // 1000)
print(1624 // 100 % 10)
print(1624 // 10 % 10)
print(1624 % 10)


def proportion(number: int) -> str:
    number_1 = number // 1000
    number_2 = number // 100 % 10
    number_3 = number // 10 % 10
    number_4 = number % 10
    if number_1 + number_4 == number_2 - number_3:
        return "ДА"
    else:
        return "НЕТ"


number = int(input())
print(proportion(number))
