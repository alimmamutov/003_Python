class Worker:
    def __init__(self, name, surname, income):
        self.name = name
        self.surname = surname
        self._income = income

    def get_total_income(self):
        total_income = sum(self._income.values())
        return total_income


class Position(Worker):
    def __init__(self, name, surname, income, position):
        super().__init__(name, surname, income)
        self.position = position

    def get_full_name(self):
        full_name = f'Full name: {self.name} {self.surname}'
        return full_name


newWorker = Position('Ivan', 'Petrov', {'wage': 100000, 'bonus': 30000}, 'Programmer')

print(newWorker.get_full_name())
print(f'Total income: {newWorker.get_total_income()}')

newWorker = Position('Elena', 'Rosina', {'wage': 50000, 'bonus': 12000}, 'Office manager')
print(newWorker.get_full_name())
print(f'Total income: {newWorker.get_total_income()}')
