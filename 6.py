# Задание 6
slov = {}
with open('./files/text_6.txt', 'r', encoding='utf-8') as file:
    # Запаковывание строк в генератор списков
    gen = (v.replace("\n", "").split() for i, v in enumerate(file.readlines(), 1))
    for i in gen:
        # Каждую строку генератора типа: ['Fizra:', '-', '30(пр)', '-']
        # Считывание со второго элемента, проверка каждого символа 1-3 элементов на число - склеивание чисел
        # с ведущим нулём: ['0', '030', '0'], применение int: [0, 30, 0] и суммирование каждого списка
        slov[i[0]] = sum([int('0' + "".join(_ for _ in j if _.isdigit())) for j in i[1:]])
    print(slov)
