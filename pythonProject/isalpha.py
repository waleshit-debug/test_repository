# files = str(input().split())
# for f in files:
#     result = f.endwith('.py')
#     print(result)

# numbers = list(map(int, input().split()))
# max = 0
#
# for f in numbers:
#     if numbers.count(f) > max:
#         max = numbers.count(el)
#         max_el = el
#
# print(max_el)

# a = input()
# len_a = len(a)
# b = []
# len_b = len(b)
# for i in a:
#     if i.isalpha():
#         b.append(i)
#     if i.isdigit():
#         b.append(i)
# print(b)
# print(len(a) - len(b))

new_list = input().split()
count = 0
for f in new_list:
    if f.isalpha():
        continue
    elif f == '#':
        continue
    elif f == '!':
        continue
    else:
        count += 1
print(count)