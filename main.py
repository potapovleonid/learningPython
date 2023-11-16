def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories.get('1').remove('11-2')

# [documents.pop(i) for i in documents if i.get('number') == '11-2']
print(*directories.values(), sep='\n')
