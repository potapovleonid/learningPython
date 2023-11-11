number_of_ticket = 123456
number_of_ticket = number_of_ticket.__str__()


if len(number_of_ticket) == 6:
    first_sum = sum(int(i) for i in list(number_of_ticket[:3]))
    second_sum = sum(int(i) for i in list(number_of_ticket[-3:]))

    if first_sum == second_sum:
        print('Congratulation! Your ticket is lucky!')
    else:
        print('Don\'t sad you\'ll lucky next time ')

number_of_ticket = 123321
number_of_ticket = number_of_ticket.__str__()


if len(number_of_ticket) == 6:
    first_sum = sum(int(i) for i in list(number_of_ticket[:3]))
    second_sum = sum(int(i) for i in list(number_of_ticket[-33:]))

    if first_sum == second_sum:
        print('Congratulation! Your ticket is lucky!')
    else:
        print('Don\'t sad you\'ll lucky next time ')
