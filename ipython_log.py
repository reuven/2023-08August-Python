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
