# Задание 3
def my_func(n1, n2, n3):
    """ Функция принимает три числа и возвращает сумму наибольших
    """
    try:
        max_2 = [n1, n2, n3]
        max_2.sort()
        return sum(max_2[-2:])
    except:
        None



print(my_func(6, 1, -9))
