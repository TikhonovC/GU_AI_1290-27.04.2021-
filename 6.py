# Задание 6
def int_func(text=''):
    """ Функция принимает на вход строку из букв латинского алфавита и пробелов
    Возвращает ту же строку, переведя первую букву каждого слова в верхний регистр, остальные - в нижний
    Если будут встречаться символы отличные от латинского алфавита - он их отфильтрует
    """
    summ_words = ''
    try:
        words = str(text)
        words = words.lower()
        for i in words:
            if 97 <= ord(i) <= 122 or ord(i) == 32:
                summ_words += i
            else:
                print(f"Ошибка обработки символа: '{i}' ({ord(i)}), проверьте, что используется латиница и пробелы")
    except:
        print(f"Ошибка обработки строки")

    return summ_words.title()

print(int_func('ABCD Efrt JUIйo'))

# print(ord('a'), ord('z'), ord('A'), ord('Z'), ord(' '))
