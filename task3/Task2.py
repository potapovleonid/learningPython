queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]

two_words = 0
three_words = 0

for query in queries:
    if len(query.split()) == 2:
        two_words += 1
    elif len(query.split()) == 3:
        three_words += 1

print(f'Queries have two words: {two_words}\n'
      f'Queries have three words: {three_words}\n')
