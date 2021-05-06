# Задание 5
new = ''
# Создание базового списка
my_list = []
while True:
    print('*' * 50)
    # Не будем фильтровать ноль и отрицательные числа, просто предусмотрим это в тексте запроса
    new = input(f"Введите положительное число больше нуля, а для выхода - EXIT: ").strip()
    if new.upper() == 'EXIT':
        break
    # Если введённая строка представляет собой числа больше нуля, то продолжаем
    if not new.isdigit() or int(new) < 1:
        continue
    new = int(new)

    print(f"Начальный список: {my_list}")
    len_ml = len(my_list)

    # Если подобное значение уже есть в списке
    if my_list.count(new) > 0:
        # Реверс, для того, чтобы искать с конца для вставки значения последним среди одинаковых
        my_list_rev = my_list.copy()
        my_list_rev.reverse()
        # Вставка на позицию равную длине списка минус отступ от конца (до подобного значения)
        my_list.insert(len_ml - my_list_rev.index(new), new)
    # Если значение больше максимального в списке, добавление в начало
    elif len_ml < 1 or new > max(my_list):
        my_list.insert(0, new)
    # Если значение меньше минимального в списке, добавление в конец
    elif new < min(my_list):
        my_list.append(new)
    # Если значения не было в списке и оно должно быть между присутсвующих, то вставляем до значения меньше этого
    else:
        for i, v in enumerate(my_list):
            if v < new:
                my_list.insert(i, new)
                break
    new = ''
    print(f"Итоговый список: {my_list}")
