def val_checker(validator):
    def func_taker(func):
        def checker(*args, **kwargs):
            if validator(*args):
                return func(*args, **kwargs)
            else:
                raise ValueError('Валидация не пройдена', args)
        return checker
    return func_taker


@val_checker(lambda x: x > 0)
def print_str(num):
    return f'Валидация пройдена успешно: {num}'


args_list = [958, -6, 8, 0]
for arg in args_list:
    try:
        print(print_str(arg))
    except ValueError as e:
        print(e.args)
