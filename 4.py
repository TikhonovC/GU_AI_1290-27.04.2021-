# Задание 4
translate = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open('./files/text_4.txt', 'r', encoding='utf-8') as file:
    # Чтение файла
    file_read = file.readlines()
    # Генератор, формирующий новую строку с заменой первого слова
    gen = (f"{translate[v.split()[0]]} {v.split()[1]} {v.split()[2]}" for i, v in enumerate(file_read, 1))
    # Открытие на запись нового файла
    with open('./files/text_44.txt', 'w', encoding='utf-8') as file_write:
        # Запись новых строк
        for i in gen:
            file_write.write(i+"\n")
