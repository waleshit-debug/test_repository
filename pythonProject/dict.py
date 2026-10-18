dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)
for k, v in dict1.items():
    print(k, "-", v)

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = dict((var, key) for key, var in dict1.items())
# for key, var in dict2.items():
#     print(key, '-', var)

# numbers_1 = set(map(int, input().split()))
# numbers_2 = set(map(int, input().split()))
# numbers_3 = set(map(int, input().split()))
# for number in (numbers_1 & numbers_2 - numbers_3):
#     print(number)
