documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def input_doc():
    return input('Input document number: ')


def p():
    number = input_doc()
    for i in documents:
        if i.get('number') == number:
            print(f"Document owner: {i.get('name')}")
            return
    print(f'This document was not found into the database')


def s():
    number = input_doc()
    for i in directories:
        if number in directories.get(i):
            print(f'The document keeps on the shelf №{i}')
            return
    print(f'This document was not found on any shelves')


def start():
    command = input('Input command: ')
    if command == 'p':
        p()
    elif command == 's':
        s()
    else:
        print(f'This command was not found')


start()
