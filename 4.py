# Задание 4
inp = int(input(f"Введите положительное число: "))
while inp <= 0:
    print(f"Введите число больше нуля: {str(inp)}")
    inp = int(input(f"Введите положительное число: "))

len_inp = len(str(inp))
max_num = 0
i = 0
while True:
    i += 1
    if i > len_inp:
        break
    # Извлечение последней цифры
    curr_num = inp % 10
    # Усечение на последнюю цифру
    inp = inp // 10
    if curr_num > max_num:
        max_num = curr_num
    # print(f"Обработка {i} числа: {curr_num}, максимальное: {max_num}")

print(f"Максимальное число: {max_num}")
