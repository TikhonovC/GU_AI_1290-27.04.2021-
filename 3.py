# Задание 3
class MyExcept(Exception):
    pass


def num_checker(value):
    try:
        return float(value)
    except ValueError:
        raise MyExcept(f"Введено не число: '{value}'")


num_array = []
while True:
    try:
        inp_data = input("Введите число (для выхода введите: stop): ")
        if inp_data == "stop":
            raise KeyboardInterrupt
        num_array.append(num_checker(inp_data))

    except MyExcept as exception:
        print(exception)

    except KeyboardInterrupt:
        print(f"{'*' * 50}\nСформированный список: {num_array}")
        break
