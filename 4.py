# Задание 4
in_words = ''
while True:
    if len(in_words) < 1:
        print('*' * 50)
        in_words = input(f"Введите слова через пробелы: ")
        continue
    for i, v in enumerate(in_words.split()):
        print(f"Слово {i+1}: '{v[0:10]}'")
    in_words = ''
