# Задание 6
from itertools import count, cycle

# Задание 6.2:
my_list = [1, 2, 3, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
iter2 = cycle(my_list)

marker = False
# Предложение ввода числа
while True and marker is False:
    num = input(f"Введите начальное число: ")
    if num.isdigit():
        for el in count(int(num)):
            print(f"Задание 6.1, следующее число: {el}")
            print(f"Задание 6.2, следующее число: {next(iter2)}")
            next_num = input(f"Введите Enter для продолжения вывода или q для завершения: ")
            if next_num == 'q':
                marker = True
                break
    continue
