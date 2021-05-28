# Задание 1
class DateString(object):
    # На вход поступает дата день-месяц-год
    def __init__(self, str_date):
        int_date = self.date_nums(str_date)
        print(int_date, end=" ")
        self.check_date(int_date)

    @classmethod
    def date_nums(cls, str_date):
        return [int(_) for _ in str_date.split("-")]

    @staticmethod
    def check_date(int_date):
        day, month, year = int_date
        dict_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        flag = True
        if not 1000 <= year <= 3000:
            print(f"Год некорректен: {year}")
            flag = False
        if not 1 <= month <= 12:
            print(f"Месяц некорректен: {month}")
            flag = False
        elif not 1 <= day <= dict_month.get(month, 0):
            print(f"День некорректнен: {day}")
            flag = False

        print(f"Дата корректна") if flag is True else ''



my_date = DateString('28-2-2011')
my_date = DateString('24-13-3001')
my_date = DateString('24-0-2051')
my_date = DateString('31-2-2141')

print(DateString.date_nums('28-2-2011'))
