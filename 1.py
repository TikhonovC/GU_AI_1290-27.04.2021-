# Задание 1
from sys import argv

try:
    vyrab, stav, premia = argv[1:]
    print(f"ЗП сотрудника: {float(vyrab) * float(stav) + float(premia)}")
except ValueError:
    print(f"Введите три параметра цифрами:  Выработка в часах, Ставка в час, Премия")
