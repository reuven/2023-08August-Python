# IPython log file


# this is a comment. Python ignores anything starting with the # until the end of the line
# I can write as many comments as I want.
# typically, comments are used to give information to the next programmer who will work on this project.

# print is a function, it's a verb -- it does something -- and that something is display things on the screen
# print can display *anything* in Python

# after we say "print", we then use round parentheses around whatever we want to display
# if we want to display text, we need to use quotes around it, either '' or "" .
print('Hello!')   
print(2 + 5)
print('Reuven')
print(Reuven)   # no quotes? Then Python will get confused
print(Reuven
print('Reuven)
# what if I want to store my name (or someone else's name) for future use, or for reuse?
# that is where variables come in.

# if functions (like print) are verbs, then variables are pronouns referring to values.

name = 'Reuven'
name = 'Reuven'
first_name = 'Reuven'
# this is OK, but your colleagues will hate you!
first_name_of_the_instructor_for_this_course = 'Reuven'
name = 'Reuven'
print(name)
print(2 + 3)
print(10 - 5)
x = 10
y = 7

print(x + y)   # first, we do what's inside the parentheses, and we get a result
x = 'abcd'
y = 'efgh'

print(x + y)
# what happens if we try to mix different types?
# at the end of the day, our computer is just lots of 1s and 0s
# but for our purposes at a high level, we have different types of data -- each type can do different things

x = 10
y = '20'    # this is not the number 20, it is a text string with the characters 2 0

print(x + y)
n1 = 123
n2 = 456

result = n1 + n2

print(result)
print('The result was ' + result)
name = 'Reuven'
print('Hello, ' + name + '!')
name = 'Reuven'
print('Hello, ' + name + '!')
name = 'Reuven'
print('Hello,' + name + '!')
name = 'Reuven'
print('Hello, ' + name + '!')
# It's pretty boring for us to use the same values in our programs, again and again.
# We want to get input from the user, and get a bit more variety.

# The way we can do that is with the "input" function.
# We call "input" and pass (in the parentheses) a text string indicating what our question is.
# The "input" function, when it runs, stops the program, and waits for user input.
# Then "input" returns the value of whatever the user entered ,as a text string.
# It's very common to have "input" on the right of an assignment. IN other words:

# assignment always means: get the value from the right side, and assign to the variable on the left side
name = input('Enter your name: ')
print(name)
# It's pretty boring for us to use the same values in our programs, again and again.
# We want to get input from the user, and get a bit more variety.

# The way we can do that is with the "input" function.
# We call "input" and pass (in the parentheses) a text string indicating what our question is.
# The "input" function, when it runs, stops the program, and waits for user input.
# Then "input" returns the value of whatever the user entered ,as a text string.
# It's very common to have "input" on the right of an assignment. IN other words:

# assignment always means: get the value from the right side, and assign to the variable on the left side
name = input('Enter your name: ')
# It's pretty boring for us to use the same values in our programs, again and again.
# We want to get input from the user, and get a bit more variety.

# The way we can do that is with the "input" function.
# We call "input" and pass (in the parentheses) a text string indicating what our question is.
# The "input" function, when it runs, stops the program, and waits for user input.
# Then "input" returns the value of whatever the user entered ,as a text string.
# It's very common to have "input" on the right of an assignment. IN other words:

# assignment always means: get the value from the right side, and assign to the variable on the left side
name = input('Enter your name: ')
print(name)
n = input('Enter your favorite number: ')
print(n + 3)   # what will it print here?
print(n + n)
name = input('Enter your name: ')
city = input('Enter your city: ')

print('Hello, ' + name + ', from ' + city + '!')
# What if I want the above to be a bit more ... readable?
# A few years ago, Python introduced a new feature called "f-strings"
# An f-string is a string, but it can have variable and other dynamic values in it
# You define it like a regular string but with f before the opening quote.
# Inside of the string, if you have {}, any Python variable or expression can be there

print(f'Hello, {name}, from {city}!')
name = input('Please enter your name?: ') 
city = input('What city are you from?: ')
print('Hello ' + name + ' from ' + city + '! It is a pleasure to meet you!')
# what if I want to know if two things are equal?

x = 10
y = 10

# are they the same?
# we have to compare with ==

x == y   # this is a totaly different operator -- asks the question, are the two sides equal? 
x = 10
y = 9

x == y
x = 'abcd'
y = 'abcd'

x == y
10 > 5    
'hello' > 'goodbye'
# if you use > or < on strings, they are compared more or less alphabetically
'hello' > 'goodbye'
name = input('Enter your name: ')

# if looks to its right, and if the condition returns True, then the "if" block is run
# at the end of the line with "if", we have a colon
# after the colon we have an indented block that all goes together as one
# 
if name == 'Reuven':
print('Hi boss!')
rint('Nice to see you again.')
else:
    print(f'Hello, {name}. Nice to meet you.')
name = input('Enter your name: ')

# if looks to its right, and if the condition returns True, then the "if" block is run
# at the end of the line with "if", we have a colon
# after the colon we have an indented block that all goes together as one
# 
if name == 'Reuven':
    print('Hi boss!')
    print('Nice to see you again.')
else:
    print(f'Hello, {name}. Nice to meet you.')
x = input('Enter something: ')
name = input('Enter your name: ')

if name == 'Reuven':   # colon at the end of the "if"
    print('Yay!')
    print('I know you')
else:
    print('Boo!')
    print('I only want to see Reuven!')
name = input('Enter your name: ')

if name == 'Reuven':   # colon at the end of the "if"
    print('Yay!')
    print('I know you')
else:
    print('Boo!')
    print('I only want to see Reuven!')
# the "else" clause is optional -- you don't need it
# but if you don't have it, then the "if" either runs or not
# nothing happens if the if's condition is False
word1 = input('Enter word 1: ')
word2 = input('Enter word 2: ')

if word1 < word2:
    print(f'{word1} comes before {word2}')
else:
    print(f'{word2} comes before {word1}')
word1 = input('Enter word 1: ')
word2 = input('Enter word 2: ')

if word1 < word2:
    print(f'{word1} comes before {word2}')
else:
    print(f'{word2} comes before {word1}')
name = input('Enter your name: ')

if name == 'Reuven':
    print('Yay! You are the best')
elif name == 'someone else':
    print('What? That is not even a name!')
elif name == 'abcdefghij':
    print('That is even weirder!')
else:
    print(f'Nice to meet you, {name}.')
name = input('Enter your name: ')

if name == 'Reuven':
    print('Yay! You are the best')
elif name == 'someone else':
    print('What? That is not even a name!')
elif name == 'abcdefghij':
    print('That is even weirder!')
else:
    print(f'Nice to meet you, {name}.')
name = input('Enter your name: ')

if name == 'Reuven':
    print('Yay! You are the best')
elif name == 'someone else':
    print('What? That is not even a name!')
elif name == 'abcdefghij':
    print('That is even weirder!')
else:
    print(f'Nice to meet you, {name}.')
x = 10
y = 20

if x == 10 and y == 20:
    print('yes, both are what you want')
# similarly, you can use "or" to check if one condition is True

if x == 10 or y == 30 or y == 50 or x == 100:
    print('Yes, one is what you wanted')
x = 10
type(x)
x = 10
y = '20'   # string 20

x + y
# what can we do with integers?

x = 10
y = 3

x + y   # addition
x - y  # subtraction

x * y   # multiplication
x / y   # division, always returning a float
x / x
# what if I want to divide two numbers, and keep only the integer part?
x // y    # this performs the division, and cuts (doesn't round) any fractional part
x ** y   # exponentiation
x % y   # the remainder after dividing x by y
# what if x is 10, and I want to increment it by 1?

x = 10
x = x + 1   # this makes no mathematical sense... but = isn't a math operator! It's assignment!

x
# we can shorten that with:

x += 1    # this is a very common idiom
# what if I have a string in a variable, and I want to turn it into an integer?

x = 10
y = '20'   # how can I add this?

# we can always get an integer from a string by calling int() on that string
# but if the string contains non-integer values, BOOM 

int(y)   # this doesn't change y! This gives us a new integer value that we can assign to a variable

y = int(y)   # get an int value based on y, and assign back to the variable y.  
x + y
