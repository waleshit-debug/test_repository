# объявление функции
def print_sorted_hyphen(s: str) -> str:
    words_list = s.split('-')
    words_list.sort()
    print('-'.join(words_list))


# считываем данные
s = 'orange-apple-avocado-plum-cherry'


# вызываем функцию
print_sorted_hyphen(s)