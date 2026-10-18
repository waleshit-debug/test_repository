def greater_half(number: int) -> int:
    round_half = number % 2
    if round_half == 0:
        return(number//2)
    else:
        return(number - number//2)
    # или решается через сумму остатка от деления и цельного результата деления
    
number = int(input())

print(greater_half(number))