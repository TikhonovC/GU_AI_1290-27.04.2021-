# Задание 3
class Cell:

    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        print("Сумма ячеек: ", end="")
        return Cell(self.count + other.count)

    def __sub__(self, other):
        print("Разность ячеек: ", end="")
        if other.count < self.count:
            return Cell(self.count - other.count)
        else:
            print("В первой клетке меньшее ячеек чем о второй.")

    def __mul__(self, other):
        print("Произведение ячеек: ", end="")
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        print("Деление ячеек: ", end="")
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
cell_3 = Cell(12)

print(cell_1 + cell_2)      # 3 + 2 = 5
print(cell_1 - cell_2)      # 3 - 2 = 1
# print(cell_3 - cell_1)      # 1 - 2 = 1
print(cell_1 * cell_2)      # 3 * 2 = 6
print(cell_1 / cell_2)     # 3 // 2 = 1

print(cell_3.make_order(maxr=5))


print(int(5.9))