# Задание 1
def delit(a, b):
    """ Функция реализует процедуру деления:
            a: Делимое
            b: Делитель
        Возвращается два аргумента:
            Результат (или None)
            Сообщение с результатом или ошибкой
    """
    try:
        a, b = str(a), str(b)
        result = round(int(a)/int(b), 3)
        mess = f"Получены числа: '{a}' и '{b}' результат деления: '{result}'"
        return result, mess
    except:
        mess = f"ОШИБКА ДЕЛЕНИЯ, проверьте аргументы: '{a}' и '{b}'"
        return None, mess



while True:
    num = ['', '']
    print('*' * 50)
    for i in 0, 1:
        # Предложение ввода числа
        while num[i] == '':
            num[i] = input(f"Введите {'второе' if i else 'первое'} число: ")
            continue
    result, mess = delit(a=num[0], b=num[1])
    print(mess)
