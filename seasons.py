def season(month):
    if month in (12, 1, 2):
        return 'Зима'
    elif month in (3, 4, 5):
        return 'Весна'
    elif month in (6, 7, 8):
        return 'Лето'
    elif month in (9, 10, 11):
        return 'Осень'
    else:
        return 'Сезон не определен'
    

if __name__ == "__main__":
    print (season(int(input())))