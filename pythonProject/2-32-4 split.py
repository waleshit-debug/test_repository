# path = '/Users/mike/Documents/Notes/tasks.md	'
# if '/' in path:
#    word = path.split('/')[-1]
# elif "\\" in path:
#     word = path.split('\\')[-1]
# final_word = word.split('.')
# print(final_word[0])

a = input()
if "/" in a:
    print(a.split("/")[-1].split(".")[0])
else:
    print(a.split("\\")[-1].split(".")[0])
