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
mysum()  # no arguments? No way...
mysum(10, 20, 30, 40, 50)  # here, I'm passing 5 integers *not* one list
mysum(numbers=[2,4,6,8])
# parameter:  numbers
# argument:   [2,4,6,8]

mysum(numbers=[2,4,6,8])
def hello(name):
    return f'Hello, {name}!'
# we've seen that I can call this function with a string
hello('world')
# what happens if I call this function with an integer?
hello(5)
hello([10, 20, 30])
hello(hello)   # yes, I can pass a function to itself as an argument!
# start very very small
# take very very small steps
# each step should take slowly in the direction of a full solution
# it's OK to be very optimistic, especially at the beginning

def count_characters(s, chars):
    # setup
    output = {}

    # calculation

    # report 
    return output
count_characters('hello out there', 'aeiou')
# start very very small
# take very very small steps
# each step should take slowly in the direction of a full solution
# it's OK to be very optimistic, especially at the beginning

def count_characters(s, chars):
    # setup
    output = {}

    # set up output to have keys from chars, and values will just be 0
    for one_character in chars:
        output[one_character] = 0

    # calculation

    # report 
    return output
count_characters('hello out there', 'aeiou')
count_characters('hello out there', 'aeiou')
# start very very small
# take very very small steps
# each step should take slowly in the direction of a full solution
# it's OK to be very optimistic, especially at the beginning

def count_characters(s, chars):
    # setup
    output = {}

    # set up output to have keys from chars, and values will just be 0
    for one_character in chars:
        output[one_character] = 0

    # calculation
    # go through our input string, s
    for one_character in s:

    # if the character appears in our dictionary
        if one_character in output:
    # then bump up the character by 1.
            output[one_character] += 1

    # report 
    return output
count_characters('hello out there', 'aeiou')
def highest_and_lowest(numbers):
    # setup
    highest = 100_000_000_000
    lowest = -100_000_000_000

    # calculation

    # report
    return [highest, lowest]
highest_and_lowest()
highest_and_lowest([10, 20, 30])
def highest_and_lowest(numbers):
    # setup
    highest = -100_000_000_000
    lowest = 100_000_000_000

    # calculation
    for one_number in numbers:
        if one_number > highest:    # is the current number higher than highest?
            highest = one_number    # if so, make this number the highest!

        if one_number < lowest:
            lowest = one_number

    # report
    return [highest, lowest]
highest_and_lowest([10, 20, 30])
highest_and_lowest([10, 20, 30, -5, 40, 25])
def highest_and_lowest(numbers):
    # setup
    highest = numbers[0]
    lowest = numbers[0]

    # calculation
    for one_number in numbers:
        if one_number > highest:    # is the current number higher than highest?
            highest = one_number    # if so, make this number the highest!

        if one_number < lowest:
            lowest = one_number

    # report
    return [highest, lowest]
highest_and_lowest([10, 20, 30])
highest_and_lowest([10, 20, 30, -5, 40, 25])
def highest_and_lowest(numbers):
    # setup
    highest = numbers[0]
    lowest = numbers[0]

    # calculation
    for one_number in numbers[1:]:  # compare with all numbers from index 1 to the end
        if one_number > highest:    # is the current number higher than highest?
            highest = one_number    # if so, make this number the highest!

        if one_number < lowest:
            lowest = one_number

    # report
    return [highest, lowest]
highest_and_lowest([10, 20, 30])
highest_and_lowest([10, 20, 30, -5, 40, 25])
# older version

# vowels, digits, and others

vowels = []
digits = []
others = []

s = input('Enter string: ').strip()

for one_character in s:
    if one_character.isdigit():
        digits.append(one_character)

    elif one_character in 'aeiou':
        vowels.append(one_character)

    else:
        others.append(one_character)

print(vowels)
print(digits)
print(others)
def dvo(s):
    # setup
    counts = {'vowels':0,
              'digits':0,
              'others':0}
    
    for one_character in s:
        if one_character.isdigit():
            counts['digits'] += 1
    
        elif one_character in 'aeiou':
            counts['vowels'] += 1
    
        else:
            counts['others'] += 1
    
    # report
    return counts
dvo('hello out there!')
dvo('hello out there! 1234')
# what if we do want to have lists of characters, and not counts of characters?

def dvo(s):
    # setup
    counts = {'vowels':[],
              'digits':[],
              'others':[]}
    
    for one_character in s:
        if one_character.isdigit():
            counts['digits'].append(one_character)
    
        elif one_character in 'aeiou':
            counts['vowels'].append(one_character)
    
        else:
            counts['others'].append(one_character)
    
    # report
    return counts
dvo('hello out there! 1234')
