import re

pattern_auto_number = r'^[A-Z]{1}\d{3}[A-Z]{2}\d{2,3}$'


def check_valid_auto_number(number: str):
    result = re.findall(pattern_auto_number, number)
    return [
        {'Number': result[0][0:6]},
        {'Region': result[0][6:]}] if result else f"Number: {number} isn't valid"


def check_valid_auto_numbers():
    print(check_valid_auto_number('A555AA1'))
    print(check_valid_auto_number('B555BB22'))
    print(check_valid_auto_number('B555BB333'))
    print(check_valid_auto_number('a555AA'))
    print(check_valid_auto_number('A555Aa'))
    print(check_valid_auto_number('A555'))
    print(check_valid_auto_number('555AA'))
    print(check_valid_auto_number('Ы555AA'))
    print(check_valid_auto_number('A555ФФ'))
    print(check_valid_auto_number('Ф555ЫЫ'))


pattern_email = r'^[\w-]{4,}@([\w-]+\.)[\w]+$'


def check_valid_email(email: str):
    return f'Email {email} is {True}' if re.findall(pattern_email, email) else f'Email {email} is {False}'


def check_valid_emails():
    print(check_valid_email('potapo!v-lv@mail.ru'))
    print(check_valid_email('pota*pov-lv@mail.ru'))
    print(check_valid_email('potapo!v-lv@mail.ru'))
    print(check_valid_email('pota$po!v-lv@mail.ru'))
    print(check_valid_email('potapolv-lv@mail.ru'))
    print(check_valid_email('potap%o!v-lv@mail.ru'))


check_valid_auto_numbers()
check_valid_emails()
