# def new_function(number):
#     if number in range(1, 3) and number % 2 == 0:
#         result = 'Два'
#     elif number == 5:
#         result = 'Пять'
#     else:
#         result = 'Bad'
#     return (result)
#
#
# number = int(input())
# print(new_function(number))


def function7(num1, num2=7):
    if num1 % num2 == 0:
        result = 'Good'
    else:
        result = 'Bad'
    return result

print(function7(int(input())))
