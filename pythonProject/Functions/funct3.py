# put your python code here
def new_function():
    count = 0
    vowels = {'а', 'у', 'о', 'и', 'э', 'ы', 'я', 'ю', 'е', 'ё'}
    word = str(input())
    for letter in word:
        if letter.lower() in vowels:
            count += 1
    print(count)

new_function()