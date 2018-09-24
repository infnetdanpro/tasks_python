#https://pythonworld.ru/osnovy/tasks.html №7

import datetime

def date(year, month, day):
    try:
        if datetime.date(year, month, day):
            return True
    except:
        return False


if __name__ == '__main__':
    print(date(2012, 11, 30))