class Car:
    def __init__(self, color: str = 'White', name: str = 'Default car', is_police: bool = False):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = ''
        print(f'The car {self.name} has been initialized')

    def go(self, speed: int = 60):
        self.speed = speed
        self.direction = 'Forward'
        print(f'The car {self.name} goes {self.direction.lower()}. Speed: {self.speed}')

    def stop(self):
        self.speed = 0
        self.direction = ''
        print('The car stopped')

    def turn(self, direction: str):
        self.direction = direction
        print(f'The car {self.name} changed direction: {self.direction.lower()}.')

    def show_speed(self):
        print(f"{self.name}'s speed: {self.speed}")


class TownCar(Car):
    def __init__(self, color: str, name: str):
        super().__init__(color, name, False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Too FAST!')
        else:
            print('Normal speed')


class WorkCar(Car):
    def __init__(self, color: str, name: str):
        super().__init__(color, name, False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Too FAST!')
        else:
            print('Normal speed')


class SportCar(Car):
    def __init__(self, color: str, name: str, is_police: bool = False):
        super().__init__(color, name, is_police)


class PoliceCar(SportCar):
    def __init__(self, color: str, name: str):
        super().__init__(color, name, True)


newTownCar1 = TownCar('Yellow', 'YellowTownCar')
newTownCar2 = TownCar('Blue', 'BlueTownCar')
newTownCar1.go()
newTownCar2.go(40)
newTownCar2.turn('Left')
newTownCar2.show_speed()
newTownCar2.go(65)
newTownCar2.show_speed()
newTownCar2.stop()
newWorkCar = WorkCar('Black', 'Black worker')
newWorkCar.go(70)
newWorkCar.show_speed()
newWorkCar.stop()
newWorkCar.show_speed()
newWorkCar.go(45)
newWorkCar.show_speed()
