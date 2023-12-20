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


pattern_email = r'^[\w-]{4,}@([\w-]{2,}\.)[a-zA-Z]{2,4}$'


def check_valid_email(email: str):
    return f'Email {email} is {True}' if re.findall(pattern_email, email) else f'Email {email} is {False}'


def check_valid_emails():
    print(check_valid_email('potapo!v-lv@mail.ru'))
    print(check_valid_email('pota*pov-lv@mail.ru'))
    print(check_valid_email('potapo!v-lv@mail.ru'))
    print(check_valid_email('pota$po!v-lv@mail.ru'))
    print(check_valid_email('potapolv-lv@mail.ru'))
    print(check_valid_email('potap%o!v-lv@mail.ru'))


pattern_remove = r'\b(\w+)( \1\b)+'


def remove_duplicate(line: str):
    return re.sub(pattern_remove, r'\1', line)


def check_remove_duplicates():
    print(remove_duplicate('I need need to learn regex regex from scratch.'))
    print(remove_duplicate('I need need need to learn regex from scratch.'))
    print(remove_duplicate('I need need to learn regex regex regex regex regex from scratch.'))
    print(remove_duplicate('I need need to to to learn regex regex from scratch.'))
    print(remove_duplicate('I need need to learn regex regex from scratch scratch.'))


pattern_mobile_number = r'^(\+7)(\d{3})(\d{3})(\d{2})(\d{2})$'
pattern_mobile_number_actual = r'\1(\2)-\3-\4-\5'


def check_valid_mobile_number(number: str):
    return re.sub(pattern_mobile_number, pattern_mobile_number_actual, number)


def check_valid_mobile_numbers():
    print(check_valid_mobile_number(r'+79876543211'))
    print(check_valid_mobile_number(r'+7986543211'))
    print(check_valid_mobile_number(r'+798654321113'))


check_valid_auto_numbers()
check_valid_emails()
check_remove_duplicates()
check_valid_mobile_numbers()
