# def climbStairs(n: int) -> int:
#     def ways(n):
#         if n <= 2:
#             return n
#         else:
#             return ways(n - 1) + ways(n - 2)
#
#     return ways(n)
#
# n = int(input("Введите количество ступеней: "))
# print(f"Количество способов подняться по лестнице: {climbStairs(n)}")

x = 121
y = str(x)[::-1]
z = int(y)
print(x == z)