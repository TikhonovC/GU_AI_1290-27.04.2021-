# Задание 2
class Road:
    """Класс расчёта массы асфальта"""
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def massa(self, mass1, height):
        mess = f"Длина: {self._length} м.\nШирина: { self._width} м.\nМасса 1кв.м.: {mass1} кг.\nВысота: {height} см.\n"
        print(mess)
        mass = self._length * self._width * mass1 * height
        return mass


rc = Road(20, 5000)
print(rc.massa(25, 5))
