def new_function():
    name = str(input())
    text = 'любит Python'
    print(name, text)


new_function()


# put your python code here
def new_function2(number, a=1):
    while a < number - 1:
        a += 1
        if number % a == 0:
            print("Bad")
            break
    else:
        print("Good")


new_function2(int(input()))
