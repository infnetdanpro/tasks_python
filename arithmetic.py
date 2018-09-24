def arithmetic(a, b, c):
    if c == '+':
        oper_ab = a + b
    elif c == '-':
        oper_ab = a - b
    elif c == '*':
        oper_ab = a * b
    elif c == '/':
        oper_ab = a / b
    else:
        oper_ab = 'Неизвестная операция'

    return oper_ab


if __name__ == "__main__":
    argunments = arithmetic(30, 5, '-')
    print (argunments)
