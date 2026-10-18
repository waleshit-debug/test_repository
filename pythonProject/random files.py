import random

open("series.txt", "w").close()
series_list = ("Кибердеревня", "Black Books", "IT Crowd", "House MD", "X-Files")
file = open("series.txt", "a")
for f in series_list:
    file.write(f"{f}\n")
file.close()
file2 = open("series.txt", "r")
lines = file2.readlines()
random = random.randint(0, len(series_list))
print(f"Сегодня можно посмотреть сериал {lines[random]}")
