# Задание 4
def my_func(x, y):
    """  Функция возводит x в отрицательную степень y
    x - положительное число
    y - отрицательное число
    """
    try:
        if x <= 0 or y >= 0:
            return None
        result1 = x**y

        result2 = x
        for i in range(abs(y)-1):
            result2 *= x
        return result1, 1/result2
    except:
        None


print(my_func(2, -31))
