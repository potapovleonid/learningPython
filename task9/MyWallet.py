def move_money(out_wallet, in_wallet, value):
    if out_wallet is Wallet and in_wallet is Wallet:
        out_wallet.top_down_money(value)
        in_wallet.add_money(value)


class Wallet:
    def __init__(self, currency, owner, money: int = 0):
        if currency not in ('USD', 'RUB', 'EURO'):
            raise ValueError(f'ERROR type currency {currency}')
        self.__currency = currency
        self.__money = money
        self.__owner = owner

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
            print(f'{self.__owner} moves transaction to {in_wallet.get_owner()} by summ {value}')
            in_wallet.add_money(value)

    def info(self):
        return f'{self.__owner} has {self.__money} {self.__currency}'

    def get_owner(self):
        return self.__owner


w1 = Wallet('USD', 'Jimm', 50, )
w2 = Wallet('USD', 'Helena', 50, )
w1.top_down_money(50)
w1.add_money(500)
w1.top_down_money(50)
w1.move_money(w2, 100)
