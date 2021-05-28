# Задание 2
class MyExcept(Exception):
    pass

inp_data = input("Введите положительное число: ")

try:
    if inp_data == '0':
         raise MyExcept("Нельзя делить на 0")
    result = 1 / int(inp_data)

except ValueError:
    print("Вы ввели не число")
except MyExcept as err:
    print(f"*** {err} ***")
else:
    print(f"Вычисление успешно: {result}")
