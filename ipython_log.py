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
# I define the function, including naming its parameters
def hello(first_name, last_name):
    return f'Hello, {first_name} {last_name}!'

# I call the function, passing values in the parentheses
hello('Reuven', 'Lerner')

# if I were to say hello(first_name, last_name), Python would say -- what are those?
def calc(n1, op, n2):
    if op == '+':
        result = n1 + n2
    elif op == '-':
        result = n1 - n2
    else:
        result = f'Illegal operator {op}'

    return f'{n1} {op} {n2} = {result}'   # return isn't a function -- no (), but they don't hurt
# our "calc" function now expects to get three arguments
# those three arguments will be assigned to our three parameters (n1, op, n2)

# By the time we get to the "if" in the function, n1, op, and n2 have
# the same values as they would have with input. This is just more elegant

calc(10, '+', 3)
# our "calc" function now expects to get three arguments
# those three arguments will be assigned to our three parameters (n1, op, n2)

# By the time we get to the "if" in the function, n1, op, and n2 have
# the same values as they would have with input. This is just more elegant

answer = calc(10, '+', 3)
print(answer)
def calc(n1, op, n2):
    if op == '+':
        result = n1 + n2
    elif op == '-':
        result = n1 - n2
    else:
        result = f'Illegal operator {op}'

    return f'{n1} {op} {n2} = {result}'   # return isn't a function -- no (), but they don't hurt
# parameters: n1,   op,  n2
# arguments:  10     '+'   3

calc(10, '+', 3)
# what happens if I call calc now with zero arguments (like we used to do?)

calc()  
# there is another kind of argument -- keyword arguments

# parameters: first_name, last_name
# arguments:  'Reuven', 'Lerner'   (positional)

hello('Reuven', 'Lerner')
#  I can do this in another way, with keyword arguments
# keyword arguments all have the form of NAME=VALUE, including the =

# parameters:  first_name     last_name
# arguments:     'Reuven'        'Lerner'

hello(first_name='Reuven', last_name='Lerner')
hello(last_name='Lerner', first_name='Reuven')
hello(las_name='Lerner', firsttt_name='Reuven')
def mysum(numbers):
    total = 0

    for one_number in numbers:
        total += one_number

    return total
mysum([10, 20, 30, 40, 50])
mysum([1,2,3,4,5])
