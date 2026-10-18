numbers = list(map(int, input().split()))
iterations = 0
numbers.sort()
while iterations < len(numbers):
    if iterations == len(numbers)-2:
        print(numbers[iterations])
        break
    else:
        iterations += 1