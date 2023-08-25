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
# what if I want to just say "randint"?

# I can't right now:

randint
# I can you randint, only under the namespace of "random"
# If want to call randint by itself, rather than via its module, can I?

from random import randint 

# This makes it possible to invoke "randint" without "random".

randint(0, 100)

# I can you randint, only under the namespace of "random"
# If want to call randint by itself, rather than via its module, can I?

from random import randint 

# This makes it possible to invoke "randint" without "random".

randint(0, 100)
# I can you randint, only under the namespace of "random"
# If want to call randint by itself, rather than via its module, can I?

from random import randint 

# This makes it possible to invoke "randint" without "random".

randint(0, 100)
# let's make this a function now:

import string

def count_punctuation(s):
    total = 0
    
    for one_character in s:
        if one_character in string.punctuation:
            total += 1
    
    print(total)
normal_punctuation
count_punctuation
count_punctuation('hello out there!')
count_punctuation('hello out there?!?')
# let's use from..import syntax now

from string import punctuation

def count_punctuation(s):
    total = 0
    
    for one_character in s:
        if one_character in punctuation:
            total += 1
    
    print(total)
count_punctuation('hello! hello?')
# let's assume that you use randint in your module.
# you could say

from random import randint

# what if we have another function variable whose name is the same? Then we will have a namespace collsion!

# First: This is why namespaces exist, so we can work without having to worry about variable names colliding.
# BUT I've heard from companies where basically outlaw the use of "from .. import" because it leads to great
# ambiguity, that the names are no longer conextualized.
# let's assume that you use randint in your module.
# you could say

from random import randint

# what if we have another function variable whose name is the same? Then we will have a namespace collsion!

# First: This is why namespaces exist, so we can work without having to worry about variable names colliding.
# BUT I've heard from companies where basically outlaw the use of "from .. import" because it leads to great
# ambiguity, that the names are no longer conextualized.

# We have another solution: We can alias our module or its imported name

import random as r   # the idea is that "r" is an alias to our random module.
random
r
random is r
import numpy as np
import pandas as pd
# aliases can be conventions

import numpy as np
import pandas as pd
pattern = '*.txt'

glob.glob(pattern)
import glob

pattern = '*.txt'

glob.glob(pattern)
from glob import glob

pattern = '*.txt'

glob(pattern)
for one_filename in glob(pattern):
    print(one_filename)
for one_filename in glob(pattern):
    print(open(one_filename).readline())
for one_filename in glob(pattern):
    print(one_filename)
    print(f'\t{open(one_filename).readline()}')
for one_filename in glob(pattern):
    print(one_filename)
    for one_line in open(one_filename):
        print(one_line)
        break
import mymod
