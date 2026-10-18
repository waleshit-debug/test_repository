# put your python code here
new_list = input().split()
search_text = input()
if (search_text in new_list) or (search_text.title() in new_list) or (search_text.lower() in new_list):
    print('Good')
else:
    print('Bad')


# new_list = input().split()
# name_input = input()
# for n in new_list:
#     if name_input.lower() == n.lower():
#         print("Good")
#         break
# else:
#     print("Bad")