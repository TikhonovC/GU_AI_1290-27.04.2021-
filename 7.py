# Задание 7
class Compl(object):
    """Класс для работы с комплексными числами"""
    def __init__(self, real=1, mnim=1):
        self.real = float(real)
        self.mnim = float(mnim)

    def __str__(self):
        """Отображение комплексного числа"""
        return str(round(self.real, 1)) + str(" + " if self.mnim > 0 else " - ") + str(abs(round(self.mnim, 1))) + "i"

    def __add__(self, other):
        """
        Перегрузка операции сложения.
        Сложение производится поэлементно
        """
        return Compl(self.real + other.real, self.mnim + other.mnim)

    def __mul__(self, other):
        """Перегрузка умножения"""
        return Compl(self.real * other.real - self.mnim * other.mnim, self.real * other.mnim + other.real * self.mnim)


####################################################
"""Операции над комплексными числами"""
a = Compl(1, 2)
b = Compl(3, -4)

print(f"a = {a}")
print(f"b = {b}")

print(f"a + b = {a + b}")
print(f"a * b = {a * b}")
