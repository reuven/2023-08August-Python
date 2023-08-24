# IPython log file


def myfunc():
    print('Hello!')
myfunc()
def calc():
    n1 = input('Enter first number: ').strip()
    op = input('Enter operator: ').strip()
    n2 = input('Enter second number: ').strip()

    n1 = int(n1)
    n2 = int(n2)

    if op == '+':
        result = n1 + n2
    elif op == '-':
        result = n1 - n2
    else:
        result = f'Illegal operator {op}'

    print(f'{n1} {op} {n2} = {result}')
calc()
calc()
def calc():
    print('2 + 3 = 4')
calc()
def calc():
    print('2 + 2 = 4')
calc()
def calc():
    n1 = input('Enter first number: ').strip()
    op = input('Enter operator: ').strip()
    n2 = input('Enter second number: ').strip()

    n1 = int(n1)
    n2 = int(n2)

    if op == '+':
        result = n1 + n2
    elif op == '-':
        result = n1 - n2
    else:
        result = f'Illegal operator {op}'

    print(f'{n1} {op} {n2} = {result}')
