# Задание 2
def personal_data(fname, lname, bdate, city, email, phone):
    """ Метод реализует процедуру получения и склеивания персональных данных
    """
    try:
        fname, lname, bdate, city, email, phone = str(fname), str(lname), str(bdate), str(city), str(email), str(phone)
        result = f"Имя: '{fname}', " \
                 f"Фамилия: '{lname}', " \
                 f"Год рождения: '{bdate}', " \
                 f"Город проживания: '{city}', " \
                 f"E-Mail: '{email}', " \
                 f"Телефон: '{phone}'"
        return result
    except:
        return None



while True:
    dic = {"Имя": '', "Фамилия": '', "Год рождения": '', "Город проживания": '', "E-Mail": '', "Телефон": ''}
    print('*' * 50)
    for i in dic:
        # Предложение ввода элемента персональных данных'
        while dic[i] == '':
            dic[i] = input(f"Введите '{i}': ")
            continue

    result = personal_data(dic['Имя'], dic['Фамилия'], dic['Год рождения'], dic['Город проживания'], dic['E-Mail'],
                           dic['Телефон'])
    print(result)
