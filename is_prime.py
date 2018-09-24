#https://pythonworld.ru/osnovy/tasks.html №6

def is_prime(number):
    if number in (range(0, 1001)):
        return isinstance(number, int)
    else:
        return False    

if __name__ == "__main__":
    number = 1000
    #try 999.0 or 1001
    print(is_prime(number))