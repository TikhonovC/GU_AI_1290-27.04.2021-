# Задание 5
from random import randint
# Генерация списка случайных чисел
range_int = [randint(1, 10) for i in range(10)]


with open('./files/text_5.txt', 'w', encoding='utf-8') as file_obj:
    # Раскрытие списка и запись в файл
    print(*range_int, sep=", ", file=file_obj)

# Открытие файла на чтение
with open('./files/text_5.txt', 'r', encoding='utf-8') as file_read:
    # Чтение строки
    first_line = file_read.readline()
    # Преобразоование строки в список, удаление перевода на следующую строку, int над сначениями и их суммирование
    print(f"Сумма элементов: {range_int}\n" + str(sum(map(int, first_line.replace("\n", "").split(", ")))))
