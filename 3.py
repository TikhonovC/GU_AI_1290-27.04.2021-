# Задание 3
class Cell:
    """ Класс для операций над клетками"""
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        print("Сумма клеток: ", end="")
        return Cell(self.count + other.count)

    def __sub__(self, other):
        print("Разность клеток: ", end="")
        if other.count < self.count:
            return Cell(self.count - other.count)
        else:
            return "В первой клетке меньшее клеток чем во второй."

    def __mul__(self, other):
        print("Произведение клеток: ", end="")
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        print("Деление клеток: ", end="")
        return Cell(int(self.count / self.count))

    def __str__(self):
        return str(self.count)


    def make_order(self, maxr):
        cnt = 1
        result = ''
        for _ in range(self.count):
            if cnt <= maxr:
                result += "*"
            else:
                result += "\n*"
                cnt = 1
            cnt += 1
        return result


cell_1 = Cell(3)
cell_2 = Cell(2)
cell_3 = Cell(14)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 - cell_3)
print(cell_1 * cell_2)
print(cell_1 / cell_2)

print(cell_3.make_order(maxr=5))
