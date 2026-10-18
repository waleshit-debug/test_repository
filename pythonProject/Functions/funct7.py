def even(num):
    result1 = 'ЧЕТ'
    return result1


def odd(num):
    result2 = 'НЕЧЕТ'
    return result2


def logic(num):
    if num % 2 == 0:
        print(even(num))
    else:
        print(odd(num))


logic(int(input()))
