def new_function():
    number = int(input())
    # использовать текст в команде input: number = input('Type text ') -
    # допускается и иногда даже рекомендуется в программировании
    if number % 2 == 0:
        print("Good!")
    else:
        print("Bad")


new_function()
