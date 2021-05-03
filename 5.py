# Задание 5
vyr = float(input(f"Введите выручку, руб.: "))
izd = float(input(f"Введите издержки, руб.: "))

prib = vyr - izd

if prib > 0:
    print(f"Прибыль составляет: {prib:.2f} руб.")
    rent = 100 * prib / vyr
    print(f"Рентабельность составляет: {rent:.2f}%")

    sotr = int(input(f"Введите количество сотрудников: "))
    while sotr <= 0:
        print(f"Количество сотрудников должно быть больше нуля: {str(sotr)}")
        sotr = int(input(f"Введите количество сотрудников: "))

    print(f"Прибыль в расчете на одного сотрудника составляет: {prib/sotr:.2f} руб.")
else:
    print(f"Конторка убыточна на: {-prib:.2f} руб.")
