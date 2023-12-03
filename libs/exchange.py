# coding: utf-8
import requests


class Rate:
    def __init__(self, format='value', diff=False):
        self.format = format
        self.diff = diff

    def exchange_rates(self):
        """
        Возвращает ответ сервиса с информацией о валютах в виде:
        
        {
            'AMD': {
                'CharCode': 'AMD',
                'ID': 'R01060',
                'Name': 'Армянских драмов',
                'Nominal': 100,
                'NumCode': '051',
                'Previous': 14.103,
                'Value': 14.0879
                },
            ...
        }
        """
        r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return r.json()['Valute']

    def make_format(self, currency):
        """
        Возвращает информацию о валюте currency в двух вариантах:
        - полная информация о валюте при self.format = 'full':
        Rate('full').make_format('EUR')
        {
            'CharCode': 'EUR',
            'ID': 'R01239',
            'Name': 'Евро',
            'Nominal': 1,
            'NumCode': '978',
            'Previous': 79.6765,
            'Value': 79.4966
        }
        
        Rate('value').make_format('EUR')
        79.4966
        """
        response = self.exchange_rates()

        if currency in response:
            if self.format == 'full':
                return response[currency]

            if self.format == 'value':
                return response[currency]['Value']

        return 'Error'

    def eur(self):
        """Возвращает курс евро на сегодня в формате self.format"""
        currency_name = 'EUR'
        if self.diff and self.format == 'value':
            response = self.exchange_rates()
            return response[currency_name]['Value'] - response[currency_name]['Previous']
        return self.make_format(currency_name)

    def usd(self):
        """Возвращает курс доллара на сегодня в формате self.format"""
        currency_name = 'USD'
        if self.diff and self.format == 'value':
            response = self.exchange_rates()
            return response[currency_name]['Value'] - response[currency_name]['Previous']
        return self.make_format(currency_name)

    def azn(self):
        """Возвращает курс азербайджанского маната на сегодня в формате self.format"""
        currency_name = 'AZN'
        if self.diff and self.format == 'value':
            response = self.exchange_rates()
            return response[currency_name]['Value'] - response[currency_name]['Previous']
        return self.make_format(currency_name)
