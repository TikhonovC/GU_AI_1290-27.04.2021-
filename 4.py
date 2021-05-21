# Задание 4
class Car:
    """Класс автомобиля"""
    def __init__(self, speed, color, name, is_police=0):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)
        print(f"Инициализирован автомобиль (Имя: '{name}', Цвет: '{color}', Скорость: '{speed}'"
              f"{', Мусорской' if self.is_police else ''})")

    def go(self):
        print(f"Автомобиль '{self.name}' начал движение")

    def stop(self):
        print(f"Автомобиль '{self.name}' остановился")

    def turn(self, direction):
        print(f"Автомобиль '{self.name}' повернулся на{direction}")

    def show_speed(self):
        print(f"Скорость автомобиля '{self.name}': {self.speed} км/ч")


class TownCar(Car):
    """Городской автомобиль"""
    def show_speed(self):
        if self.speed > 60:
            print(f"Внимание городской автомобиль превысил разрешённую скорость в 60 км/ч: {self.speed} км/ч")
        else:
            print(f"Скорость автомобиля '{self.name}': {self.speed} км/ч")


class SportCar(Car):
    """Спортивный автомобиль"""
    pass


class WorkCar(Car):
    """Рабочий автомобиль"""
    def show_speed(self):
        if self.speed > 40:
            print(f"Внимание рабочий автомобиль превысил разрешённую скорость в 40 км/ч: {self.speed} км/ч")
        else:
            print(f"Скорость автомобиля '{self.name}': {self.speed} км/ч")


class PoliceCar(Car):
    """Мусорской автомобиль"""
    def __init__(self, speed, color, name, is_police=1):
        super().__init__(speed, color, name, is_police)


print("*" * 50)
car1 = TownCar(name="Городской", color="Красный", speed=70)
car1.go()
car1.turn("лево")
car1.show_speed()
car1.stop()
print("*" * 50)

car2 = SportCar(name="Спорт", color="Зелёный", speed=70)
car2.go()
car2.turn("право")
car2.show_speed()
car2.stop()

print("*" * 50)
car3 = WorkCar(name="Рабочий", color="Жёлтый", speed=50)
car3.go()
car3.turn("прямо")
car3.show_speed()
car3.stop()

print("*" * 50)
car4 = PoliceCar(name="Мусора", color="Жёлтый", speed=80)
car4.go()
car4.turn("зад")
car4.show_speed()
car4.stop()
