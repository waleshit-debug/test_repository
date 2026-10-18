from self import self


def lesser_number(n_1: int, n_2: int, n_3: int, n_4: int) -> int:
    list_1 = [n_1, n_2, n_3, n_4]
    list_1.sort()
    return list_1[0]


n_1 = 3
n_2 = 1
n_3 = 3
n_4 = 5

print(lesser_number(n_1, n_2, n_3, n_4))