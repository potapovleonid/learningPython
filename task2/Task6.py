stream = [
    'user4,2021-01-01;3',
    'user3,2022-01-07;4',
    'user2,2022-03-29;1',
    'user1,2020-04-04;13',
    'user2,2022-01-05;7',
    'user1,2021-06-14;4',
    'user3,2022-07-02;10',
    'user4,2021-03-21;19',
    'user4,2022-03-22;4',
    'user4,2022-04-22;8',
    'user4,2021-05-03;9',
    'user4,2022-05-11;11'
]
sum_watches = 0
users = []

for date in stream:
    user, watches = date.split(',')[0], date.split(';')[1]
    sum_watches += int(watches)
    if user not in users:
        users.append(user)

print(f'Average watches on user: {sum_watches/len(users)}')

stream = [
    'user100,2022-01-01;150',
    'user99,2022-01-07;205',
    'user1001,2022-03-29;81'
]

sum_watches = 0
users = []

for date in stream:
    user, watches = date.split(',')[0], date.split(';')[1]
    sum_watches += int(watches)
    if user not in users:
        users.append(user)

print(f'Average watches on user: {sum_watches / len(users)}')
