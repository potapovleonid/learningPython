import re

tweet = 'когда #эпидемия, то обязательно #оставайсядома'

print(re.findall(r'#\w+', tweet))

date = '1st september 2019 17:25'

print(re.findall(r'\d{1,2}\w{0,2}\s\w+\s\d{4}\s\d{1,2}:\d{1,2}', date))

messages = ['Опять дождь! Лайков: 5, Репостов: 4', 'Крутой был концерт! Лайков: 28, Репостов: 22']

likes = 0
reposts = 0
likes_pattern = r'Лайков:\s\d+'
repost_pattern = r'Репостов:\s\d+'

for i in messages:
    if re.findall(likes_pattern, i):
        like = int(re.findall(r'\d+', re.findall(likes_pattern, i)[0])[0])
        likes += like

    if re.findall(repost_pattern, i):
        repost = int(re.findall(r'\d+', re.findall(repost_pattern, i)[0])[0])
        reposts += repost

print(f'Likes: {likes}, Reposts: {reposts}')

tweet_23 = 'Какое замечательное место! Обязательно вернусть сюда снова. Всем советую!!!'
print(re.split(r'[!?.]+\s', tweet_23))

'''

'''
passwords = ['Apple34!rose', 'My87hou#4$', 'abc123']
res = []
for i in passwords:
    # if re.findall(r'[*#$%!&.][a-zA-Z][0-9]', i) and 8 <= len(i) <= 20:
    if re.findall(r'[\w*#$%!&.]{8,20}', i):
        res.append(i)

print(res)

report = 'файл 11.txt загружен, файл 22.txt загружен, файл 33.txt ошибка'

file_download = r'\d+\.txt(?=\sзагружен)'
file_error = r'\d+\.txt(?!\sзагружен)'
print(re.findall(file_download, report))
print(re.findall(file_error, report))

prices = 'RUB4.44, RUB10.88, EUR0.99, RUB99.99'
list_prices = re.findall(r'(?<=RUB)[0-9.]+', prices)
print(sum(float(i) for i in list_prices))
