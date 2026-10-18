# text1 = input()
# file1 = open('file.txt', 'w')
# file1.write(text1)
# file1.close()
# file2 = open('file.txt', 'r')
# print(file2.read())
# import lines

# import shutil
# value_1 = input()
# with open('file_1.txt','w') as file:
#     file.write(value_1)
# with open('file_2.txt', 'w') as file:
#     shutil.copy('file_1.txt', 'file_2.txt')
# with open('file_2.txt', 'r') as file:
#     print(file.readline())

# films = input().split()
# open('file.txt', 'w').close()
# file1 = open('file.txt', 'a')
# for f in films:
#     file1.write(f'{f}\n')
# file1.close()
# file2 = open('file.txt', 'r')
# lines = file2.readlines()
# for i in range(len(lines)):
#     print(lines[i].strip())
#     if i < len(lines) - 1:
#         print("*****")

# import random
# series_list = ('Кибердеревня', 'Black Books', 'IT Crowd', 'House MD', 'X-Files')
# file = open('series.txt', 'a')
# for f in series_list:
#     file.write(f'{f}\n')
# file.close()
# file2 = open('series.txt', 'r')
# lines = file2.readlines()
# random = random.randint(0, len(series_list))
# print(f'Сегодня можно посмотреть сериал {lines[random]}')

# numbers = list(map(int, input().split()))
# with open('file.txt', 'w') as file:
#     for n in numbers:
#         file.write(f'{n}\n')
# with open('file.txt', 'r') as file:
#     result = sum(int(file.strip()) for f in file)
# print(result)

# open('file1.txt', 'w').close()
# open('file2.txt', 'w').close()
# numbers = list(map(int, input().split()))
# with open('file1.txt', 'w') as file1:
#     for f in numbers:
#         file1.write(f'{f}\n')
# with open('file1.txt', 'r') as file1, open ('file2.txt', 'a') as file2:
#     lines = list(map(int, file1.readlines()))
#     lines.sort(reverse=True)
#     for f in lines:
#         file2.write(f'{f}\n')
# with open('file2.txt', 'r') as file2:
#     print(file2.read())

films = input().split()
set_films = set(films)
dicti = {}

# word_count = {}
# with open("file_1.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         movie = line.strip()
#         if movie in word_count:
#             word_count[movie] += 1
#         else:
#             word_count[movie] = 1
# sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

with open("file1.txt", "w") as file1:
    for f in films:
        file1.write(f"{f}\n")
with open("file1.txt", "r") as file1:
    lines = file1.readlines()
    for film in set_films:
        dicti[film] = lines.count(f"{film}\n")
sorted_dicti = sorted(dicti.items(), key=lambda item: item[1], reverse=True)
for key, var in sorted_dicti:
    print(key, "-", var)
