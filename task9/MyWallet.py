def move_money(out_wallet, in_wallet, value):
    if out_wallet is Wallet and in_wallet is Wallet:
        out_wallet.top_down_money(value)
        in_wallet.add_money(value)


class Wallet:
    def __init__(self, currency, money: int = 0):
        if currency not in ('USD', 'RUB', 'EURO'):
            raise ValueError(f'ERROR type currency {currency}')
        self.__currency = currency
        self.__money = money

    def add_money(self, value: int):
        self.__money += value
        print(self.info())

    def top_down_money(self, value: int):
        if self.__money < value:
            raise ValueError(f'You have not enough money. {self.info()}')
        self.__money -= value
        print(self.info())

    def move_money(self, in_wallet, value):
        if type(in_wallet) is Wallet:
            self.top_down_money(value)
            in_wallet.add_money(value)

    def info(self):
        return f'You have {self.__money} {self.__currency}'


w1 = Wallet('USD', 50)
w2 = Wallet('USD', 50)
w1.top_down_money(50)
w1.add_money(500)
w1.top_down_money(50)
print('_')
w1.move_money(w2, 100)
