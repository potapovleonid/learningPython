boys = sorted(['Peter', 'Alex', 'John', 'Arthur', 'Richard'])
girls = sorted(['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'])

if len(list(boys)) == len(list(girls)):
    print(f'Perfect couples:')
    for boy, girl in zip(boys, girls):
        print(f'{boy} and {girl}')
else:
    print(f'Quantity boys and girls isn\'t equal')

boys = sorted(['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael'])
girls = sorted(['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'])

if len(list(boys)) == len(list(girls)):
    print(f'Perfect couples:')
    for boy, girl in zip(boys, girls):
        print(f'{boy} and {girl}')
else:
    print(f'Quantity boys and girls isn\'t equal')