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
def finalvers(yourinput):
    mydict= {'digits':0 , 'vowels':0, 'others':0}
    
    for words in yourinput:
        if words.isdigit():
            mydict['digits']+= 1
            
        elif words in 'aeiou':
            mydict['vowels'] += 1
            
        else:
            mydict['others'] += 1
            
        
        return mydict

finalvers('hello! 123')
def finalvers(yourinput):
    mydict= {'digits':0 , 'vowels':0, 'others':0}
    
    for words in yourinput:
        if words.isdigit():
            mydict['digits']+= 1
            
        elif words in 'aeiou':
            mydict['vowels'] += 1
            
        else:
            mydict['others'] += 1
            
        
        return mydict

finalvers('ello! 123')
def finalvers(yourinput):
    mydict= {'digits':0 , 'vowels':0, 'others':0}
    
    for words in yourinput:
        if words.isdigit():
            mydict['digits']+= 1
            
        elif words in 'aeiou':
            mydict['vowels'] += 1
            
        else:
            mydict['others'] += 1
            
        
    return mydict

finalvers('hello! 123')
# we can use the "help" function in Jupyter

help(len)    # we don't execute len. We just pass it (the function object) to "help"
help(str.lower)
def hello(name):
    return f'Hello, {name}!'
help(hello)
# rewritten with a docstring

def hello(name):
    '''
    hello is a friendly function that returns a greeting with your name.

    expects: a string, the name of the user (to be used in the output)
    modifies: - 
    returns: a nice and friendly string
    '''
    return f'Hello, {name}!'
help(name)
help(hello)
s = 'abcd'
print(s)
s = 'abcd
efgh'
print(s)
s = '''abcd
efgh'''
print(s)
def dvo(s):
    '''
    dvo: counts the digits, vowels, and others in a string

    Expects: An argument of a string
    Modifies: -
    Returns: A dictionary with three keys (vowels, digits, others) and the count of 
        each type of character in the dict values.
    '''
    
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
dvo('whatever 123')
help(dvo)  # we don't execute the function
import random
help(random.randint)   # the function we used on Monday..
def analyze_word(one_word):
    if one_word[0] == one_word[0].lower():
        is_lowercase == True
    else:
        is_lowercase == False

    return is_lowercase, len(one_word)   # this is a totally acceptable tuple
analyze_word('hello')
def analyze_word(one_word):
    if one_word[0] == one_word[0].lower():
        is_lowercase = True
    else:
        is_lowercase = False

    return is_lowercase, len(one_word)   # this is a totally acceptable tuple
def analyze_word(one_word):
    if one_word[0] == one_word[0].lower():
        is_lowercase = True
    else:
        is_lowercase = False

    return is_lowercase, len(one_word)   # this is a totally acceptable tuple
analyze_word('hello')
t = analyze_word('hello')
t
# when we get a tuple back, it's very common to grab the parts of it with unpacking
is_lc, length = analyze_word('hello')
is_lc
length
def get_status():
    return 200, 50, {'timing':30, 'logged_in': False}
get_status()
status_code, bytes_returned, info_dict = get_status()
status_code
bytes_returned
info_dict
info_dict['timing']
def add(first, second):
    return first + second

add(10, 3)
add(10)
# what if I want to have the option of passing a second argument.. or of not doing so?

# this where default values come in

# parameters: first second
# argumentse:   10     3

add(10, 3)
def add(first, second=10):
    return first + second
add(5, 4)
# parameters: first second
# arguments:   5      4
add(5, 4)
# when we define the function, we tell Python what the default value should be
# for second, if we don't pass it a value

def add(first, second=10):
    return first + second
# parameters: first second
# arguments:   5      4
add(5, 4)
# parameters: first  second
# arguments:   5   

add(5)
# parameters: first  second
# arguments:   5       10

add(5)
def add(first=10, second):
    return first + second
def add(first=3, second=4):
    return first + second

add(10, 6)
add(10)
add()
# is there a way for me to call add, passing a value to second?
# we can use a keyword argument

add(second=10)
s = '    a   b   c  d   '

s.strip()
# I can tell it to remove all whitespace, plus a nd d from their usual 
s.strip(' a d')
# earlier, we together developed count_characters

# I want you to modify this function such that "chars" has a default of vowels, but
# you can pass any string to have those characters counted. So pass 'aeiou' to have vowels counted, etc.

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
# earlier, we together developed count_characters

# I want you to modify this function such that "chars" has a default of vowels, but
# you can pass any string to have those characters counted. So pass 'aeiou' to have vowels counted, etc.

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
count_characters('hello out there')
count_characters('hello out there', 'aeiou')
count_characters('hello out there', 'asdfg')
