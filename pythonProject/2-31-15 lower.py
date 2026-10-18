word = input()
if len(set(word.lower())) == len(word.lower()):
    print('Bad')
    print(set(word))
else:
    print('Good')