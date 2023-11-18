sequence = '2 3 1 5 9 22 3 5'


def even_or_add(str_of_elements):
    list_elements = [int(x) for x in str_of_elements.split(' ')]
    even_list = [x for x in list_elements if x % 2 == 0]
    odd_list = [x for x in list_elements if x % 2 == 1]
    print(f'Even numbers: {len(even_list)}\n'
          f'Odd numbers: {len(odd_list)}')

    print(*even_list)
    print(*odd_list)

    print(even_list[0])

    if len(even_list) > len(odd_list):
        print(f'Index of first excess odd number: {list_elements.index(odd_list[0])}')
    else:
        print(f'Index of first excess even number: {list_elements.index(even_list[0])}')


even_or_add(sequence)
