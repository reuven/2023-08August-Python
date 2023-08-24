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
def hello():
    return f'Hello out there!'
print('Hello out there')
hello()
# get the value back from hello, and then print it
print(hello())
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

    return f'{n1} {op} {n2} = {result}'   # return isn't a function -- no (), but they don't hurt
calc()
x = calc()
print(x)
def hello():
    name = input('Enter your name: ').strip()

    return f'Hello, {name}!'
hello()
greeting = hello()
print(greeting)
def hello(name):                # define hello with one parameter, called "name"
    return f'Hello, {name}!'    # we can assume that "name" was assigned a value via an argument

print(hello('Reuven'))
