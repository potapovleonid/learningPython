year = 2020

if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print(year.__str__() + ': isn\'t leap-year')
else:
    print(year.__str__() + ': is leap-year')

year = 2019

if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print(year.__str__() + ': isn\'t leap-year')
else:
    print(year.__str__() + ': is leap-year')

year = 2000

if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print(year.__str__() + ': isn\'t leap-year')
else:
    print(year.__str__() + ': is leap-year')

year = 1900

if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print(year.__str__() + ': isn\'t leap-year')
else:
    print(year.__str__() + ': is leap-year')
