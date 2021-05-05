# Задание 1
list_1 = [1, 1.1, complex(5, 6), b'text', bytearray(b'1 0'), "2", True, None, {1, 2}, frozenset('1'),
          {"a": 1, "b": 2}, (1, 2), [1, 2]]

for i, v in enumerate(list_1):
    print(f"{i}-й аргумент '{v}' имеет тип: '{str(type(v))[8:-2]}'")
