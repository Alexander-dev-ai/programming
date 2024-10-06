def sm(a, b):
    return a + b


def raz(a, b):
    return a - b


def ml(a, b):
    return a * b


def dl(a, b):
    return a / b


a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
op = input('Введите одну из четырёх операций (-,+,/,*): ')

if op == '+':
    print(sm(a,b))
elif op == '-':
    print(raz(a,b))
elif op == '/':
    if b != 0:
        print(dl(a,b))
    else:
        print('На ноль делить нельзя')
elif op == '*':
        print(a * b)
