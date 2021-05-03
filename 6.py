# Задание 6
day = 0
while True:
    a = float(input(f"Введите дистанцию первого дня (a), км.: "))
    b = float(input(f"Введите порог дистанции (b), км.: "))
    if a <= 0 or b < 0:
        print(f"Дистанция первого дня должна быть больше нуля ({a}>0), а порог не равен нулю ({b}=>0)")
        print("*" * 50)

    else:
        while True:
            # print(f"День {day}, дистанция: {a}")
            a = a + a * 0.1
            day += 1
            if a > b:
                print(f"На {day} день путь превысит {b} км., составя: {a:.2f} км.")
                break
        break
