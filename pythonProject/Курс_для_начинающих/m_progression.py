# Арифмети́ческая прогре́ссия — последовательность чисел (членов прогрессии), в которой каждое число,
# начиная со второго, получается из предыдущего добавлением к нему постоянного числа d (шага, или разности прогрессии)
# Вычисляется по формуле an = a1 + (n - 1)*d

def progression_3(number_1: int, number_2: int, number_3: int) -> str:
    if (number_2 - number_1) == (number_3 - number_2):
        return "YES"
    else:
        return "NO"


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
print(progression_3(number_1, number_2, number_3))
