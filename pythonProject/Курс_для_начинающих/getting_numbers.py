# 1

def get_numbers_1 (input_value: int) -> str:
    first_number = input_value // 100
    second_number = (input_value // 10) % 10
    third_number = input_value % 10
    summ_numbers = first_number + second_number + third_number
    mult_numbers = first_number * second_number * third_number

    return f"Сумма цифр = {summ_numbers}\nПроизведение цифр = {mult_numbers}"

# 2
def get_numbers_2 (input_value: int) -> str:
    a = input_value // 100
    b = (input_value // 10) % 10
    c = input_value % 10

    return f"{a}{b}{c}\n{a}{c}{b}\n{b}{a}{c}\n{b}{c}{a}\{c}{a}{b}\{c}{b}{a}"

input_value = int(input())
print(get_numbers_2(input_value))