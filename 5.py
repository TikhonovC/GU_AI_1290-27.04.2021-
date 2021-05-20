# Задание 5
class Stationery:
    """Класс автомобиля"""
    def __init__(self, title="Название"):
        self.title = title

    def draw(self):
        """Метод отрисовки"""
        print(f"Запуск отрисовки '{self.title}'")




class Pen(Stationery):
    """Класс ручки"""
    def draw(self):
        """Метод отрисовки"""
        print(f"Запуск отрисовки '{self.title}' ручкой")

class Pencil(Stationery):
    """Класс карандаша"""
    def draw(self):
        """Метод отрисовки"""
        print(f"Запуск отрисовки '{self.title}' карандашом")

class Handle(Stationery):
    """Класс маркера"""
    def draw(self):
        """Метод отрисовки"""
        print(f"Запуск отрисовки '{self.title}' маркером")


pen = Pen()
pen.draw()

pencil = Pencil('рисунок')
pencil.draw()

handle = Handle('разметку')
handle.draw()


