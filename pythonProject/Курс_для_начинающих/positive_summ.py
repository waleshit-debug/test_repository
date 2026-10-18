def plus_summ(number_1: int, number_2: int, number_3: int) -> str:
    numbers_list = [number_1, number_2, number_3]
    summ = 0
    for f in numbers_list:
        if f > 0:
            summ += f
        else:
            continue
    return summ


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(plus_summ(number_1, number_2, number_3))