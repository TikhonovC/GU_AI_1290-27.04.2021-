# Задание 4-6
class Sklad(object):
    """Класс Склад оргтехники"""
    def __init__(self):
        """Инициализация склада"""
        self.dic_items = {}

    def add_item(self, add_items_dict):
        """Добавление на склад"""
        # Проверка словаря
        self.check_dict(add_items_dict)
        # Для каждой позиции проверка, что есть и добавление в переменные
        for i, v in add_items_dict.items():
            if i in self.dic_items:
                self.dic_items[i] += v
            else:
                self.dic_items[i] = v
        print(f"На склад успешно добавлены: {str(add_items_dict)}")

    def get_item(self, get_items_dict):
        """Перемещение со склада"""
        # Проверка словаря
        self.check_dict(get_items_dict)
        print(f"Перемещение со склада: {get_items_dict}")
        for i, v in enumerate(get_items_dict):
            if v in self.dic_items:
                if self.dic_items[v] < int(get_items_dict[v]):
                    raise MyExcept(f"Недостаточно '{v}': '{self.dic_items[v]}', а всего '{get_items_dict[v]}'")
                else:
                    self.dic_items[v] -= get_items_dict[v]
            else:
                raise MyExcept(f"Нет запрашиваемой техники: {str(BasOrg(v).name)}")

    def __str__(self):
        """Статистика по складу"""
        return (f"На складе: {str(self.dic_items)}")

    @staticmethod
    def check_dict(inp):
        """Проверяет валидность востушившего словаря с техникой"""
        if inp is None or len(inp) < 1:
            raise MyExcept(f"Передан пустой словарь: '{str(inp)}'")
        for i in inp:
            if inp[i] is None or type(inp[i]) != int or int(inp[i]) < 1:
                raise MyExcept(f"Ошибка во входящем словаре: '{str(i)}: {str(inp[i])}'")


###########################################################################
class BasOrg(object):
    """Базовый класс для оргтехники"""
    def __init__(self, name):
        self.name = str(name)


class Printer(BasOrg):
    """Дочерний класс для Принтера"""
    def __init__(self):
        return super().__init__("Принтер")


class Scanner(BasOrg):
    """Дочерний класс для Сканера"""
    def __init__(self):
        return super().__init__("Сканер")


class Xerox(BasOrg):
    """Дочерний класс для Ксерокса"""
    def __init__(self):
        return super().__init__("Ксерокс")


class MyExcept(Exception):
    """Кастомное исключение"""
    def __init__(self, text):
        self.text = str(text)

    def __str__(self):
        return f"*** {self.text} ***"



#############################################################################
""" Перемещение техники по шагам"""
sklad = Sklad()
try:
    print("\n--- Добавление оргтехники на склад ---")
    add_items_dict = {Printer().name: 10, Scanner().name: 11, Xerox().name: 12}
    sklad.add_item(add_items_dict)
    print(sklad)
except MyExcept as exception:
    print(exception)

try:
    print("\n--- Перемещение со склада ---")
    get_items_dict = {Printer().name: 1, Scanner().name: 3, Xerox().name: 5}
    sklad.get_item(get_items_dict)
    print(sklad)
except MyExcept as exception:
    print(exception)

try:
    print("\n--- Перемещение со склада (Прогнозируемая ошибка)---")
    get_items_dict = {Printer().name: 100, Scanner().name: 3, Xerox().name: 5}
    sklad.get_item(get_items_dict)
    print(sklad)
except MyExcept as exception:
    print(exception)
finally:
    print(sklad)

try:
    print("\n--- Добавление оргтехники на склад (Прогнозируемая ошибка) ---")
    add_items_dict = {Printer().name: 0, Scanner().name: 8, Xerox().name: 7}
    sklad.add_item(add_items_dict)
    print(sklad)
except MyExcept as exception:
    print(exception)
finally:
    print(sklad)

try:
    print("\n--- Перемещение со склада (Прогнозируемая ошибка) ---")
    get_items_dict = {Printer().name: 0, Scanner().name: 4, Xerox().name: 3}
    sklad.get_item(get_items_dict)
    print(sklad)
except MyExcept as exception:
    print(exception)
finally:
    print(sklad)
