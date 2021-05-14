# Задание 7
from math import factorial
def fact(number):
    for i in range(1, number+1):
        yield f"{i}! = {factorial(i)}"




# Предложение ввода числа
while True:
    num = input(f"Введите начальное число: ")
    if num.isdigit():
        num = int(num)
        for el in fact(num):
            print(el)
    continue
