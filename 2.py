# Задание 2
from random import randint
# my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_list = [randint(0, 100) for i in range(10)]

new_list = [val for k, val in enumerate(my_list) if k > 0 and val > my_list[k-1]]
print(f"Исходный список: {my_list}")
print(f"Новый список: {new_list}")

