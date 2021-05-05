# Задание 6
# Инициализация переменных
new_goods = {}
dict_names = {}
dict_names = {"название": ("Название товара", "str"),
              "цена": ("Цену товара", "int"),
              "количество": ("Количество товара", "int"),
              "eд": ("Единицу измерения товара", "str")}
# Инициализация суммарного списка
goods = []
# Инициализация флага выхода
flag_exit = False
# Инициализация нумерации элементов суммарного списка
num = 1
# Основной цикл
while flag_exit is False:
    print('*' * 40 + " Для выхода введите: --EXIT--")
    # Цикл с предложением ввести значение элемента и проверок
    for i, v in enumerate(dict_names):
        new_goods[v] = ''
        # Бесконечный цикл с предложением ввода и проверками - если проверки прошли успешно, то предложение ввода
        # следующего атрибута
        while new_goods[v] == "" and flag_exit is False:
            new_goods[v] = input(f"Введите {dict_names[v][0]}: ").strip()
            # Блок для выхода из программы
            if new_goods[v].upper() == '--EXIT--':
                flag_exit = True
                break
            # Проверки введённых значений
            # Проверка, что цена и количество - цифры
            if dict_names[v][1] == "int" and not new_goods[v].isdigit():
                print(f"'{dict_names[v][0]}' должно быть целым числом")
                new_goods[v] = ""
                continue
            # Проверка, что Название и ед. изм. - не пустые
            elif dict_names[v][1] == "str" and len(new_goods[v]) < 1:
                print(f"'{dict_names[v][0]}' должно содержать хотя бы один символ")
                new_goods[v] = ""
                continue
            else:
                break
    # Если все введённые значения прошли проверки - добавление в список
    goods.append((num, new_goods))
    # Увеличение счётчика нумерации списка
    num += 1
    # Вывод текущего состояния списка
    print(goods) if flag_exit is False else None
    # Очистка вводимых значений для следующей итерации в while
    new_goods.clear()
