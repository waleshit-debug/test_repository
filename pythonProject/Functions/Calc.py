print('Для вычислений введите число, математический символ (+ , - , / , *) и второе число')

def calc(num1, sign, num2):
    allowed_signs = ['+', '-', '/', '*']
    if sign not in allowed_signs:
        print('Для вычислений используйте между числами один из символов: + (плюс), - (минус), / (разделить) или * (умножить)')
    if sign == '+':
        print(plus(num1, num2))
    elif sign == '-':
        print(minus(num1, num2))
    elif sign == '*':
        print(multiply(num1, num2))
    elif sign == '/':
            print(divide(num1, num2))

def plus(num1, num2):
    result = num1 + num2
    return result

def minus(num1, num2):
    result = num1 - num2
    return result

def multiply(num1, num2):
    result = num1 * num2
    return result

def divide(num1, num2):
    result = num1 / num2
    return result

try:
    num1 = float(input())
    sign = input()
    num2 = float(input())
    calc(num1, sign, num2)
except ZeroDivisionError:
    print('Деление на ноль возвращает ошибку')
except ValueError:
    print('Для вычисления используйте целые числа или числа с разделителем . (точка)')
except NameError:
    print('Для вычисления используйте целые числа или числа с разделителем . (точка)')
