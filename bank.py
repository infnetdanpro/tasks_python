#https://pythonworld.ru/osnovy/tasks.html №5
def bank(deposit, years):
    i = 0
    while i < years:
        deposit = deposit * 0.01 + deposit
        i += 1
    return round(deposit, 2)
    

if __name__ == "__main__":
    deposit = int(input('Введите сумму депозита: '))
    years = int(input('Введите количество лет: '))
    print ('Расчет по ставке 10% годовых: ')
    print(bank(deposit, years))
