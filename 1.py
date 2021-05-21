# Задание 1
import time
from itertools import cycle
from random import randint


class TrafficLight:
    """Класс светофора"""
    __color = {"Красный": 7, "Жёлтый": 2, "Зелёный": randint(1, 3), "*" * 50: 0}

    def running(self):
        """Метод переключения световора"""
        for color in cycle(self.__color):
            print(color + (f" (задержка: {self.__color[color]})" if self.__color[color] > 0 else ''))
            time.sleep(self.__color[color])


svetofor = TrafficLight()
svetofor.running()
