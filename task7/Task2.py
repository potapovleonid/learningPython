class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def up(self):
        self.salary += 100
    def print(self):
        print(f"Employee's {self.name}, his salary is: {self.salary}")


e = Employee('Joh', 2500)
e.print()
e.up()
e.print()
