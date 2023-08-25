# IPython log file


import random
# what did we get in the module object?
type(random)
# what can we do with a module object?
# not much! We can retrieve items from its attributes:

random.randint(0, 10)    # because "randint" is a function defined in the "random" module
# what can we do with a module object?
# not much! We can retrieve items from its attributes:

random.randint(0, 10)    # because "randint" is a function defined in the "random" module
# what if you don't know what attributes are available?
dir(random)
# given a string, count the punctuation marks
s = 'He is really a what?!?'
total = 0

for one_character in s:
    if one_character in string.punctuation:
        total += 1

print(total)
# given a string, count the punctuation marks
import string
s = 'He is really a what?!?'
total = 0

for one_character in s:
    if one_character in string.punctuation:
        total += 1

print(total)
random.randint(0, 100)
