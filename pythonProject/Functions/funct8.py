def function8(full_name):
    name_list = full_name.split(' ')
    surname = (name_list[0]) + ' '
    name1 = (name_list[1][0]) + '.'
    name2 = (name_list[2][0]) + '.'
    result = surname + name1 + name2 #или result = f'{name_list[0]} {name_list[1][0]}.{name_list[2][0]}.'
    return result


full_name = str(input())
print(function8(full_name))
