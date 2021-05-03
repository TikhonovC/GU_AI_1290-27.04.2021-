# Задание 2
inp = int(input(f"Введите время в секундах: "))

while inp < 0:
    print(f"Введите число больше нуля: {str(inp)}")
    inp = int(input(f"Введите время в секундах: "))

hours = inp // (60 * 60)
minutes = inp // 60 - hours * 60
seconds = inp % 60

print(f"{hours:02}:{minutes:02}:{seconds:02}")
