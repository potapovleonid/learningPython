class Wallet:
    def __init__(self, currency, money: int = 0):
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

    def info(self):
        return f'You have {self.__money} {self.__currency}'


w1 = Wallet('USD', 50)
w1.top_down_money(50)
w1.add_money(500)
w1.top_down_money(50)
