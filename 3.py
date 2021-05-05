# Задание 3
month = 0
while True:
    if month not in range(1, 13):
        month = int(input(f"Введите месяц цифрой от 1 до 12: "))
        continue
    # Список
    list_calend = [range(1, 3), "Зима", range(3, 6), "Весна", range(6, 9), "Лето", range(9, 12), "Осень", [12], "Зима"]
    for i, v in enumerate(list_calend):
        # Гоним по чётным элементам и проверяем, что введённый месяц входит в range
        if i % 2 == 0 and month in v:
            print(f"Время года по месяцу №{month} из списка: {list_calend[i+1]}")
    # Словарь
    dict_calend = {"Зима": [1, 2, 12], "Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11]}
    for i in range(4):
        dk, dv = dict_calend.popitem()
        print(f"Время года по месяцу №{month} из словаря: {dk}") if month in dv else None

    month = 0
