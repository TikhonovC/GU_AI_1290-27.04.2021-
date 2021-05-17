# Задание 1
with open('./files/file1.txt', 'w', encoding='utf-8') as file:
    while True:
        new_line = input(f"Введите новую строку для записи в файл: ")
        if new_line == '':
            break
        try:
            file.write(f"{new_line}\n")
            print(f"Записано: {new_line}")
        except IOError:
            print("Ошибка записи строки")
