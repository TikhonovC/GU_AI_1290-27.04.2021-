# Задание 2
from abc import ABC, abstractmethod


class Odezhda(ABC):
    """ Родительский класс ля одежды - суммирует и форматирует результат"""
    def __init__(self, name):
        self.name = name
        self.result = 0

    @property
    @abstractmethod
    def calculate(self):
        """Пустой класс для переопределения"""
        pass

    def __add__(self, other):
        return round(self.calculate + other.calculate, 2)

    def __str__(self):
        return f"{self.name}: {self.calculate}"
###################################################################


class Palto(Odezhda):
    """ Класс для расчёта ткани по Пальто"""
    def __init__(self, size):
        super().__init__("Пальто")
        self.size = size

    @property
    def calculate(self):
        return round((self.size / 6.5) + 0.5, 2)


class Kostum(Odezhda):
    """ Класс для расчёта ткани по Костюму"""
    def __init__(self, heith):
        super().__init__("Костюм")
        self.heith = heith

    @property
    def calculate(self):
        return round((2 * self.heith + 0.3), 2)
###################################################################


palto = Palto(50)
print(palto)
kostum = Kostum(190)
print(kostum)

print(palto + kostum)
print(palto.calculate + kostum.calculate + kostum.calculate)
