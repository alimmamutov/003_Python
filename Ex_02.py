class Road:
    _length = 0
    _width = 0

    def __init__(self, _length: int, _width: int):
        self._length = _length
        self._width = _width

    def asp_mass(self, mass_for_meter: int = 25, canvas_thickness: int = 5):
        mass = int(self._width * self._length * mass_for_meter * canvas_thickness/1000)
        print(f'{mass} т')


myRoad = Road(20, 5000)
myRoad.asp_mass()
myRoad.asp_mass(20, 10)
a = 0
