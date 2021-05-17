# Задание 7
import json
slov = {}
with open('./files/text_7.txt', 'r', encoding='utf-8') as file:
    # Вычитка каждой строки с преобразованием в список
    gen = [v.replace("\n", "").split() for i, v in enumerate(file.readlines(), 1)]
    # Добавление прибыли каждой компании в словарь
    slov = {i[0]: int(i[2]) - int(i[3]) for i in gen}
    result = \
        [slov, {"average_profit": sum([i for i in slov.values() if i > 0]) /
                                  len([i for i in slov.values() if i > 0])}]
# Запись результата в json
with open('./files/text_7.json', 'w', encoding='utf-8') as file_json:
    json.dump(result, file_json, ensure_ascii=False)
