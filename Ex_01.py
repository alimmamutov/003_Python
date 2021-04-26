import random


class Matrix:
    def __init__(self, matrix_list):
        self.matrix = matrix_list
        self.columns_count = len(matrix_list[0])
        self.strings_count = len(matrix_list)

    def __str__(self):
        matrix_string = ''

        for string_number in self.matrix:
            current_str = ''
            for column_number in string_number:
                current_str = f'{current_str} {column_number}'
            matrix_string = f'{matrix_string} {current_str}\n'
        return matrix_string

    def __add__(self, other):
        if self.columns_count != other.columns_count or self.strings_count != other.strings_count:
            raise ValueError('Матрицы должны быть одной размерности')
        else:
            stringList = []
            for i in range(self.strings_count):
                columnList = []
                for j in range(self.columns_count):
                    columnList.append(self.matrix[i][j]+other.matrix[i][j])
                stringList.append(columnList)
            return stringList


def create_matrix(strings_count, columns_count):
    stringList = []
    for current_string in range(strings_count):
        columnList = []
        for current_column in range(columns_count):
            columnList.append(random.randint(-100, 100))
        stringList.append(columnList)
    return stringList


matrix_1 = Matrix(create_matrix(3, 2))
matrix_1_1 = Matrix(create_matrix(3, 2))
print(matrix_1)
print(matrix_1_1)

matrix_2 = Matrix(create_matrix(3, 3))
print(matrix_2)

matrix_3 = Matrix(create_matrix(2, 4))
print(matrix_3)

matrix_4 = Matrix(matrix_1 + matrix_1_1)
print(matrix_4)
