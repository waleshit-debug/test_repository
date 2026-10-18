import math


def math_operations():
    value_1 = int(input())
    value_2 = int(input())
    summ_values = value_1 + value_2
    extract_values = value_1 - value_2
    multiplicate_values = value_1 * value_2
    divide_values = value_1 / value_2
    divide_round_values = value_1 // value_2  # целое от деления
    divmod_values = value_1 % value_2  # остаток от деления
    square_values = math.sqrt(value_1 ** 10 + value_2 ** 10) # возведение в степень имеет самый высокий приоритет
    square_values = math.sqrt(value_1 ** 10 ** value_2) # возведение в степень вычисляется справа налево (сначала знач2, потом знач1)                                                      
    operations_list = [
        summ_values,
        extract_values,
        multiplicate_values,
        divide_values,
        divide_round_values,
        divmod_values,
        square_values,
    ]
    for f in operations_list:
        print(f)


math_operations()
