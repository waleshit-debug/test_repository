# url = input().split()
# url_list_1 = []
# for f in url:
#     f_list = f.split('/')
#     for f in f_list:
#         if 'www' in f:
#             f = f[(f.find('.'))+1:]
#             url_list_1.append(f)

for f in url_list_1:
    print(f)

    url = input().split()
    url_list_1 = []
    counter = 0
    most_often = 0
    for f in url:
        f = f.replace('https://', '').replace('http://', '').replace('www.', '')
        f = f.split('/')[0]
        url_list_1.append(f)

    for f in url_list_1:
        frequency = url_list_1.count(f)
        if frequency > counter:
            counter = frequency
            most_often = f
    print(most_often)