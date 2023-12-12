import re

pattern_auto_number = r'^[A-Z]{1}\d{3}[A-Z]{2}\d{2,3}$'


def check_valid_auto_number(number: str):
    result = re.findall(pattern_auto_number, number)
    return {result[0][0:6]: result[0][6:]} if result else False


def check_valid():
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


check_valid()
