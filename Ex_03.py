def type_logger(function):
    def inside_type_logger(*args):
        for arg in args:
            print(f'Аргумент: {arg} имеет тип: {type(arg)}')
        return True

    return inside_type_logger


@type_logger
def calc_cube(*args):
    my_list = []
    for arg in args:
        if type(arg) == int:
            my_list.append(int(arg) ** 3)
    return my_list


calc_cube(985, 'my_string', [999, 'my_string_2'], 2.5)