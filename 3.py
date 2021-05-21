# Задание 3
class Worker:
    """Класс работника с его характеристиками """
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    """Класс для должности работника"""
    def get_full_name(self):
        full_name = f"{self.name} {self.surname}"
        return full_name

    def get_total_income(self):
        total_income = sum(self._income.values())
        return total_income


pos = Position(name="Sergei", surname="Tikhonov", position="dev", wage=30, bonus=3)
print(f"Имя: {pos.get_full_name()},\nДолжность: {pos.position},\nЗП: {pos.get_total_income()}")
