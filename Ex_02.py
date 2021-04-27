class OwnError(ZeroDivisionError):
    def __init__(self, txt):
        self.txt = txt


a = 5
b = 0
try:
    if b == 0:
        raise OwnError('Деление на ноль не допустимо')
except OwnError as err:
    print(err)
