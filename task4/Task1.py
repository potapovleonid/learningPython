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


def find_owner():
    doc_number = input('Input document number: ')
    doc_owner = get_document_owner(doc_number)
    if doc_owner is not None:
        print(f"Document owner: {doc_owner}")
    else:
        print(f'This document was not found into the database')


def get_document_owner(doc_number):
    for i in documents:
        if i.get('number') == doc_number:
            return i.get('name')
    return None


def find_storage_shelf():
    doc_number = input('Input document number: ')
    number_of_shelf = get_number_of_shelf(doc_number)
    if number_of_shelf is not None:
        print(f'The document keeps on the shelf №{number_of_shelf}')
    else:
        print(f'This document was not found on any shelves')


def get_number_of_shelf(doc_number):
    for i in directories:
        if doc_number in directories.get(i):
            return i
    return None


def list_of_documents():
    print(f'Current list of documents:')
    for i in documents:
        print(
            f"№: {i.get('number')}, type: {i.get('type')} owner: {i.get('name')}, "
            f"storage shelf: {get_number_of_shelf(i.get('number'))}"
        )


def add_shelf():
    shelf_number = input(f'Input shelf number that you want to add: ')
    for i in directories:
        if shelf_number == i:
            print(f'This shelf is already exists. {get_all_shelves_str()}')
            return
    directories.setdefault(shelf_number, [])
    print(f'Shelf №{shelf_number} added successfully. All shelves: {get_all_shelves_str()}')


def get_all_shelves_str():
    return f'All shelves: {", ".join(directories.keys())}'


def delete_shelf():
    shelf_number = input(f'Input shelf number that you want to delete: ')
    for i in directories:
        if shelf_number == i:
            del directories[shelf_number]
            print(f'Shelf №{shelf_number} deleted successfully. {get_all_shelves_str()}')
            return
    print(f'This shelf was not found. {get_all_shelves_str()}')


def add_document():
    doc_number = input('Input document number: ')
    doc_type = input('Input document type: ')
    doc_owner = input('Input document owner: ')
    doc_shelf = input('Input shelf for storage document: ')

    if doc_shelf in directories and get_document_owner(doc_number) is None:
        documents.append({'type': doc_type, 'number': doc_number, 'name': doc_owner})
        directories.get(doc_shelf).append(doc_number)
        list_of_documents()
    else:
        print(f"This shelf wasn't found. You need to add shelf using command 'as'")


def delete_document():
    doc_number = input('Input document number: ')

    if get_document_owner(doc_number) is not None:
        for i in range(len(documents)):
            if documents[i]['number'] == doc_number:
                del documents[i]
                break
        directories.get(get_number_of_shelf(doc_number)).remove(doc_number)
        list_of_documents()
    else:
        print(f"Document wasn't found")
        list_of_documents()

def move_document():
    doc_number = input('Input document number: ')
    new_doc_shelf = input('Input new shelf for storage document: ')

    if directories.get(new_doc_shelf) is None:
        print(f'This shelf was not found. {get_all_shelves_str()}')
        return

    if get_document_owner(doc_number) is None:
        print(f'This document was not found.')
        list_of_documents()
        return

    doc_shelf = get_number_of_shelf(doc_number)

    if doc_shelf == new_doc_shelf:
        print(f'Old document shelf and new document shelf are identical\n'
              f'{get_all_shelves_str()}')
        return


    if doc_shelf is not None:
        directories.get(doc_shelf)

def start():
    while True:
        command = input('Input command: ')
        if command == 'p':
            find_owner()
        elif command == 's':
            find_storage_shelf()
        elif command == 'l':
            list_of_documents()
        elif command == 'ads':
            add_shelf()
        elif command == 'ds':
            delete_shelf()
        elif command == 'ad':
            add_document()
        elif command == 'd':
            delete_document()
        elif command == 'm':
            move_document()
        elif command == 'exit':
            break
        else:
            print(f'This command was not found')


start()
