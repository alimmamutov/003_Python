class MyExceptionClass(Exception):
    def __init__(self, txt):
        self.txt = txt


elements = []
while True:
    try:
        element = input('Введите число (STOP - для выхода)')
        if element.upper() == "STOP":
            break
        if not element.isdigit():
            raise MyExceptionClass("Введено не число!")
        elements.append(element)
    except MyExceptionClass as err:
        print(f'Были введены числа:{err}')
print(elements)
