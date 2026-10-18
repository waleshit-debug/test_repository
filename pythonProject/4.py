text = str('В тот самый час, когда он перестал бороться, судьба ему улыбнулась.')
char_list = [' ', ',', '.', '!', ':', ';']
iteration = 0
for f in text:
    iteration += 1
    if f not in char_list:
        continue
    else:
        if iteration >= 30:
            print(f'{text[:text.index(f, iteration - 1)]}!')
            break

# text = input()
# for f in range(30, len(text)):
#     if text[f] == ' ':
#         print(text[:f] + '!')
#         break

