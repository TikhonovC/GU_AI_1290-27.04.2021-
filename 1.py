# Задание 1
import time
from itertools import cycle
from random import randint


class TrafficLight:
    __color = {"Красный": 7, "Жёлтый": 2, "Зелёный": randint(1, 3)}

    def running(self):
        for color in cycle(self.__color):
            print(color + f" (задержка: {self.__color[color]})")
            time.sleep(self.__color[color])


svetofor = TrafficLight()
svetofor.running()