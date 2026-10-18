def new_function():
    numbers = list(map(int, input().split()))
    max_number = max(numbers)
    if len(numbers) < 2:
        print('Bad')
    else:
        for f in numbers:
            if f == max_number:
                print(f)
                numbers.remove(f)
        print(max(numbers))


new_function()

# def new_function(radius, pi=3.14):
#     print(int(radius**2 * pi))
#
#
# new_function(int(input()))

