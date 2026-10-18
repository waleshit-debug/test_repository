# var = input()
# try:
#     number = int(var)
#     print(number)
# except ValueError:
#     print("Невозможно преобразовать строку в целое число")

# my_list = [10, 20, 30, 40, 50]
# var = int(input())
# try:
#     print(my_list[var])
# except IndexError:
#     print('Индекс вне диапазона')

var1 = int(input())
var2 = int(input())
my_list = [0, 2, 4]

try:
    result = my_list[var1] / my_list[var2]
    print(result)
except IndexError:
    print("Индекс вне диапазона")
except ZeroDivisionError:
    print("Деление на ноль недопустимо")
