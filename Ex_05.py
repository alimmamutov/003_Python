class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Рисуем ручкой {self.title}'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Рисуем карандашом {self.title}'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Рисуем маркером {self.title}'


stationary = Stationary('Default stationary')
pen = Pen('My pen 1')
pencil = Pencil('My pencil 1')
handle = Handle('My handle 1')
print(stationary.draw())
print(pen.draw())
print(pencil.draw())
print(handle.draw())