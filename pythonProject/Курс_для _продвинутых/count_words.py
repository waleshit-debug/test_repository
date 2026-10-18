def count_words():
    incoming_string = str(input())
    words_list = incoming_string.split()
    words_counter = len(words_list)
    print(words_counter)


count_words()
