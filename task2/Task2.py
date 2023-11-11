sum_of_numbers = 0
while True:
    value = int(input('Input number: '))
    if value != 0:
        sum_of_numbers += value
    else:
        print(f'Sum: {sum_of_numbers}')
        break
