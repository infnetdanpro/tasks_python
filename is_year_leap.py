#https://pythonworld.ru/osnovy/tasks.html #2
def is_year_leap(year):
    if (year % 4) != 0:
        return 'Обычный год'
    elif (year % 100) == 0:
        if (year % 400) == 0:
            return 'Високосный год'
        else:
            return('Обычный')
    else:
        return 'Високосный год'

if __name__ == "__main__":
    try:
        print('Введите цифрами год: ')
        view_leap_year = is_year_leap(int(input()))
        print (view_leap_year)
    except:
        print('Ошибка расчетов')
