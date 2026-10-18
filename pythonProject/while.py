# # put your python code here
# numbers = list(map(int, input().split()))
# index = 0
# while numbers[index] % 2 == 0:
#     print(numbers[index])
#     index += 1

# numbers = list(map(int, input().split()))
# index = 0
# while numbers[index] > 7:
#    print(numbers[index])
#    index += 1


def is_it_prime(n):
    divider = 2
    while n % divider != 0:
        divider += 1
    if divider == n:
        print(n)


f = int(input())
is_it_prime(f)