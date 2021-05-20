# Задание 2
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def massa(self, mass1, height):
        mess = f"Длина: {self._length}\nШирина: { self._width}\nМасса 1см: {mass1}\nВысота: {height}\n"
        mass = self._length * self._width * mass1 * height
        return mess, mass


rc = Road(20, 5000)
print(*rc.massa(25, 5))
