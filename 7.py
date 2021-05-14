# Задание 7
from math import factorial

def fact(number):
    try:
        for i in range(1, number+1):
            yield f"{i}! = {factorial(i)}"
    except:
        return None

# Предложение ввода числа
while True:
    num = input(f"Введите начальное число: ")
    if num.isdigit():
        num = int(num)
        for el in fact(num):
            print(el)
    continue
