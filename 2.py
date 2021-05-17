# Задание 2
empty_line = 0
nempty_line = 0
slov_full, slov_line = 0, 0

with open('./files/file2.txt', 'r', encoding='utf-8') as file:
    file_read = file.readlines()
    for i, v in enumerate(file_read, 1):
        slov_line = 0
        # Если строка пустая
        if v == f'\n':
            empty_line += 1
        # Если в строке есть символы кроме переноса строки
        elif len(v) > 1:
            nempty_line += 1
            slov_line = len(v.split())
            slov_full += slov_line
        print(f"{i} строка ({slov_line} слов): {v}", end="")

    print(f"\n\n*** Всего строк: {empty_line + nempty_line}, из них пустых: {empty_line}, всего слов: {slov_line} ***")
