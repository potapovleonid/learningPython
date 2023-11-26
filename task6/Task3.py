from datetime import datetime

date = 'May 25 2017 5:00AM'
date = datetime.strptime(date, '%B %d %Y %I:%M%p')
print(date)