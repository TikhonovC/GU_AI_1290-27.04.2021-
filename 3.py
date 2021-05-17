# Задание 3
with open('./files/text_3.txt', 'r', encoding='utf-8') as file:
    # Сборка файлового объекта в список
    line = [[v.split()[0], float(v.split()[1])] for i, v in enumerate(file)]
    # Расчёт средней зарплаты пробеганием по второму элементу каждого вложенного списка
    sredn = sum([v[1] for i, v in enumerate(line)])/len(line)
    # Извлечение фамилий с окладом <20 тыс.:
    # пробегание по каждому вложенному списку и извлечение первого элемента, если второй элемент меньше 20 тыс.
    nish = [f"{v[0]}" for i, v in enumerate(line, 1) if float(v[1]) < 20000]
    # print(line, "\n")
    print(f"Средняя ЗП: {sredn}, из них нищебродов: {', '.join(nish)}")
