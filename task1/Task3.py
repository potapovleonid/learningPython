day = int(input('Input day of birthday: '))
month = str(input('Input month of birthday: '))

if (21 <= day <= 31 and month.lower() == 'march') or (1 <= day <= 19 and month.lower() == 'april'):
    print('Your sign is Aries')
elif (20 <= day <= 30 and month.lower() == 'april') or (1 <= day <= 20 and month.lower() == 'may'):
    print('Your sign is Taurus')
elif (21 <= day <= 31 and month.lower() == 'may') or (1 <= day <= 21 and month.lower() == 'june'):
    print('Your sign is Gemini')
elif (22 <= day <= 30 and month.lower() == 'june') or (1 <= day <= 22 and month.lower() == 'july'):
    print('Your sign is Cancer')
elif (23 <= day <= 31 and month.lower() == 'july') or (1 <= day <= 22 and month.lower() == 'august'):
    print('Your sign is Leo')
elif (23 <= day <= 31 and month.lower() == 'august') or (1 <= day <= 22 and month.lower() == 'september'):
    print('Your sign is Virgo')
elif (23 <= day <= 30 and month.lower() == 'september') or (1 <= day <= 23 and month.lower() == 'october'):
    print('Your sign is Libra')
elif (24 <= day <= 31 and month.lower() == 'october') or (1 <= day <= 21 and month.lower() == 'november'):
    print('Your sign is Scorpius')
elif (22 <= day <= 30 and month.lower() == 'november') or (1 <= day <= 21 and month.lower() == 'december'):
    print('Your sign is Sagittarius')
elif (22 <= day <= 31 and month.lower() == 'december') or (1 <= day <= 19 and month.lower() == 'january'):
    print('Your sign is Capricorns')
elif (20 <= day <= 31 and month.lower() == 'january') or (1 <= day <= 18 and month.lower() == 'february'):
    print('Your sign is Aquarius')
elif (19 <= day <= 29 and month.lower() == 'february') or (1 <= day <= 20 and month.lower() == 'march'):
    print('Your sign is Pisces')
else:
    print('Date or month is incorrect')
