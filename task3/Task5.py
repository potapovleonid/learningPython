my_list = ['2018-01-01', 'yandex', 'cpc', 100]

while len(my_list) > 1:
    len_list = len(my_list)
    my_list = my_list[0:len_list - 2] + [{my_list[len_list - 2]: my_list[len_list - 1]}]

print(f'{my_list[0]}')

my_list = ['a', 'b', 'c', 'd', 'e', 'f']

while len(my_list) > 1:
    len_list = len(my_list)
    my_list = my_list[0:len_list - 2] + [{my_list[len_list - 2]: my_list[len_list - 1]}]

print(f'{my_list[0]}')
