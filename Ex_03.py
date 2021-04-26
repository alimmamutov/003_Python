class Cell:
    def __init__(self, cell: int):
        self.count = cell

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if self.count - other.count > 0:
            return Cell(self.count - other.count)
        else:
            raise ValueError("Разность количества ячеек двух клеток должно быть больше нуля!!!")

    def __mul__(self, other):
        newCell = Cell(self.count * other.count)
        return newCell

    def __floordiv__(self, other):
        return Cell(self.count // other.count)

    def make_order(self, num):
        s = ''
        for i in range(self.count // num):
            s += f'{"*"*num}\n'
        s += f'{"*"*(self.count % num)}'
        if not self.count % num: s = s[:-1]
        return s

    def __str__(self):
        return str(self.count)


c1 = Cell(10)
print(c1)
c2 = Cell(6)
print(c2)
c3 = c1 + c2
print(c3)
c4 = c1 - c2
print(c4)
c5 = c1 * c2
print(c5)
c6 = c1 // c2
print(c6)
print(c2.make_order(5))
a = 0
