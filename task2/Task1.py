word = 'testing'
middle_of_word = len(word) // 2

if len(word) % 2 == 0:
    if middle_of_word == 1:
        middle_of_word -= 1
    print(f'{word[middle_of_word]}{word[middle_of_word + 1]}')
else:
    print(word[middle_of_word])

word = 'test'
middle_of_word = len(word) // 2

if len(word) % 2 == 0:
    if middle_of_word == 1:
        middle_of_word -= 1
    print(f'{word[middle_of_word]}{word[middle_of_word + 1]}')
else:
    print(word[middle_of_word])

word = 'te'
middle_of_word = len(word) // 2

if len(word) % 2 == 0:
    if middle_of_word == 1:
        middle_of_word -= 1
    print(f'{word[middle_of_word]}{word[middle_of_word + 1]}')
else:
    print(word[middle_of_word])
