# Задание 1
m1 = [[1, 2, 33], [3, 4, 44], [3, 4, 44]]
m2 = [[5, 6, 66], [7, 8, 88], [7, 8, 88]]


class Matrix:
    """Класс для печати и сложения матриц"""
    def __init__(self, listing):
        self.listing = listing

    def __str__(self):
        # Транспортиование матрицы
        transp = [list(row) for row in zip(*self.listing)]
        # Раскрытие каждой строки списка с довавлением перевода на следующую строку
        a = [' '.join(map(str, ii))+"\n" for i, ii in enumerate(transp)]
        return ''.join(map(str, a))

    def __add__(self, other):
        summ_matrix = []
        for i, ii in enumerate(self.listing):
            summ_matrix.append([])
            for j, jj in enumerate(self.listing[0]):
                summ_matrix[i].append(self.listing[i][j] + other.listing[i][j])
        return Matrix(summ_matrix)


matrix_1 = Matrix(m1)
matrix_2 = Matrix(m2)
print(matrix_1)
print(matrix_2)
print('*'*50)
print(matrix_1 + matrix_2)
