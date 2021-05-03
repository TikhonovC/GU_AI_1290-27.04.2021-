# Задание 3
while True:
    inp = input(f"Введите число больше нуля: ")
    if inp > '0':
        inp2 = inp + inp
        inp3 = inp * 3

        print(f"{inp}+{inp2}+{inp3}: {int(inp) + int(inp2) + int(inp3)}")
