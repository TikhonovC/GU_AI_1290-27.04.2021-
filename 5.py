# Задание 5
from functools import reduce

def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el * el

new_list = [i for i in range(100, 1001, 2)]
# print(f"Исходный список: {my_list}")
print(f"Новый список: {new_list}")
print(f"Произведение всех элементов списка: {reduce(my_func, new_list)}")
