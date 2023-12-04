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

#1:35