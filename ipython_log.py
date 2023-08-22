# IPython log file


s = 'abcde'

# can I print all of the letters in s, each on a line of its own?
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
for one_character in s:
    print(one_character)
print('Before')
for one_character in s:
    print(one_character)
print('After')    
one_character
total = 0

s = input('Enter a string: ').strip()

for one_character in s:
    if one_character in 'aeiou':   # is the current character a vowel?
        total += 1                 # add 1 to our total!

print(total)
total = 0

s = input('Enter a string: ').strip()

for one_character in s:
    if one_character in 'aeiou':   # is the current character a vowel?
        total += 1                 # add 1 to our total!

# print(total)
print(f'{s} has {total} vowels')
# I'm in a great mood -- hooray for Python!

print('Hooray for Python!')
print('Hooray for Python!')
print('Hooray for Python!')
# we can use a loop to DRY up this code:

for counter in 3:
    print('Hooray for Python!')
for count in range(3):
    print('Hooray for Python!')
# this is how you iterate a certain number of times!

for count in range(5):
    print('Hooray for Python!')
# this is how you iterate a certain number of times!

for count in range(2):
    print('Hooray for Python!')
# this is how you iterate a certain number of times!

for count in range(0):
    print('Hooray for Python!')
# this is how you iterate a certain number of times!

for count in range(3):
    print('Hooray for Python!')
# what about count? We have a loop variable there, but what is its value with each iteration?
# count actually does get a value with each iteration -- it starts at 0, and goes up by 1, one at a time

for count in range(3):
    print(f'[{count}] Hooray for Python!')
'Hooray' * 6   # this will work!
print('Hooray') * 6
name = 'Reuven'

# how can I print a name triangle?
print(name[:1])   # index 0
print(name[:2])   # indexes 0+1
print(name[:3])   # indexes 0+1+2
print(name[:4])   # indexes 0+1+2+3
print(name[:5])   # indexes 0+1+2+3+4
print(name[:6])   # indexes 0+1+2+3+4+5
# how can I accomplish this with a for loop?

for index in range(5):
    print(name[:index])
# how can I accomplish this with a for loop?

for index in range(6):
    print(name[:index])
# how can I accomplish this with a for loop?

for index in range(6):     # iterate 6 times, getting the numbers 0-5
    print(name[:index+1])  # take that number, add 1 to it, and set it to be the max index
# let's make it general for all names

name = input('Enter your name: ').strip()

for index in range(len(name)):     # iterate 6 times, getting the numbers 0-5
    print(name[:index+1])          # take that number, add 1 to it, and set it to be the max index
# let's make it general for all names

name = input('Enter your name: ').strip()

for index in range(len(name)):     # iterate 6 times, getting the numbers 0-5
    print(name[:index+1])          # take that number, add 1 to it, and set it to be the max index
name=input('What is your name? ').strip() 

total = 0

for numOfLetters in name:
    total+=1
    print(name[:total])
# option 1 -- calculate it manually

index = 0
s = 'abcde'

for one_character in s:
    print(f'{index}: {one_character}')
    index += 1
# option 2 -- use Python's "enumerate" function
# enumerate is meant to be called (a) in a loop (b) with an iterable 

# we call enumerate, passing it the iterable as an argument
# we get back not only the original elements, but also their indexes
# the for loop is going to look REALLY weird

s = 'abcde'

for index, one_character in enumerate(s):    # we now have *TWO* loop variables! enumerate sets both
    print(f'{index}: {one_character}')
# example while loop

x = 5

while x > 0:
    print(x)
    x -= 1    # this means: x = x - 1, aka reduce x by 1
total = 0

s = input('Enter a number: ')

total += s
total = 0

s = input('Enter a number: ')

total += int(s)   # get an int based on s, then add that to total
total = 0

while total < 100:
    s = input('Enter a number: ')
    total += int(s)   # get an int based on s, then add that to total

print(f'total = {total}')
total = 0

while total < 100:
    print(f'\tTotal is currently {total}')
    s = input('Enter a number: ')
    total += int(s)   # get an int based on s, then add that to total

print(f'total = {total}')
# let's pretend that there is no "in" operator in Python
# I have a string, and want to know whether a character is in that string

s = 'abcde'
look_for = 'd'  

for one_character in s:
    if look_for == one_character:  # have we found what we want?
        break

    print(one_character)
# let's pretend that there is no "in" operator in Python
# I have a string, and want to know whether a character is in that string

s = 'abcde'
look_for = 'd'  

for one_character in s:
    if look_for == one_character:  # have we found what we want?
        break

    print(one_character)

print('Done!')
# let's pretend that there is no "in" operator in Python
# I have a string, and want to know whether a character is in that string

# in this version, we don't want to print the look_for character, but don't want to stop the loop, either.

s = 'abcde'
look_for = 'd'  

for one_character in s:
    if look_for == one_character:  # have we found what we want?
        continue  # go onto the next iteration right away

    print(one_character)

print('Done!')
total = 0

while total < 100:
    print(f'\tTotal is currently {total}')
    s = input('Enter a number: ')
    total += int(s)   # get an int based on s, then add that to total

print(f'total = {total}')
total = 0

while total < 100:
    print(f'\tTotal is currently {total}')
    s = input('Enter a number: ')
    total += int(s)   # get an int based on s, then add that to total

print(f'total = {total}')
total = 0

while total < 100:
    print(f'\tTotal is currently {total}')
    s = input('Enter a number: ')

    if s.isdigit():
        total += int(s)   # get an int based on s, then add that to total

print(f'total = {total}')
while True:     # this is scary looking -- it's an infinite loop!
    name = input('Enter your name: ').strip()

    if name == '':   # empty string (not to be confused with ' ', which has a space in it)
        break

    print(f'Hello, {name}!')
total = 0

while True:     
    s = input('Enter some digits: ').strip()

    if s == '':   # there is nothing between these quotes -- it's really the *EMPTY* string!
        break

    for one_character in s:
        if not one_character.isdigit():   # if this isn't 0-9... 
            print(f'{one_character} is not numeric!')
            continue

        total += int(one_character)

print(f'total = {total}')
total = 5

total += '3'   # here, I'm trying to add a string 
total = 5

total += int('3')  # now we're adding the int based on the digit '3' which is a string
total = 5

total += int('3')  # now we're adding the int based on the digit '3' which is a string
total
# let's create a list!
# this list contains 10 elements
# every element is an integer
# elements are separated by ,
# around the outside of the list, we use []

mylist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# there are *many* aspects of lists that are similar (or identical) to strings

mylist[0]  # get the first element
mylist[1]  # get the 2nd element
mylist[-1]  # get the final element
len(mylist)   #how many elements are there, anyway?
mylist[3:6
mylist[3:6]
mylist[3:6]  # from index 3 up to (and not including) index 6
# use a for loop on a list:

for one_item in mylist:
    print(one_item)
high_temps = [34, 33, 33, 33, 34, 32, 32, 33, 35]

# this is a list of integers
total = 0
for one_temp in high_temps:
    total += one_temp
total    
high_temps = [34, 33, 33, 33, 34, 32, 32, 33, 35]

# this is a list of integers
total = 0
for one_temp in high_temps:
    total += one_temp

total / len(high_temps)
# remember that strings are immutable

s = 'abcde'
s[0] = '!'   # this won't work!
high_temps = [34, 33, 33, 33, 34, 32, 32, 33, 35]

# this is a list of integers
total = 0
for one_temp in high_temps:
    total += one_temp

round(total / len(high_temps))
high_temps = [34, 33, 33, 33, 34, 32, 32, 33, 35]

# this is a list of integers
total = 0
for one_temp in high_temps:
    total += one_temp

round(total / len(high_temps), 2)   # round the float to the nearest number, with 2 decimal points
#  can we change lists?

mylist = [10 ,20, 30 ,40, 50]

mylist[0] = '!'
mylist
# lists are mutable!  You can change their elements!
# lists are mutable (we can change their elements)
# but we can also add new elements to them, and remove existing ones

mylist.append(60)   # this means: add the integer 60 as a new element to the end of the list
mylist
# how can I remove an element? Easiest way is with the list.pop method, which removes something
# from the end of the list, and returns it

mylist.pop()
mylist
mylist = []    # empty list
mylist.append(10)
mylist.append(20)
mylist.append(30)
mylist
vowels = []
digits = []
others = []

s = input('Enter a string: ').strip()

for one_character in s:
    print(one_character)
vowels = []
digits = []
others = []

s = input('Enter a string: ').strip()

for one_character in s:
    if one_character in 'aeiou':   # is it a vowel?
        print(f'{one_character} is a vowel')
    elif one_character.isdigit():   # is it a digit?
        print(f'{one_character} is a digit')
    else:
        print(f'{one_character} is something else')
        
vowels = []
digits = []
others = []

s = input('Enter a string: ').strip()

for one_character in s:
    if one_character in 'aeiou':   # is it a vowel?
        vowels.append(one_character)
    elif one_character.isdigit():   # is it a digit?
        digits.append(one_character)
    else:
        others.append(one_character)

print(f'digits = {digits}')
print(f'vowels = {vowels}')
print(f'others = {others}')
        
# adding more than one element to a list

mylist = [10, 20, 30]
mylist.append([40, 50, 60])  # what will happen?

mylist
len(mylist)
# if we want to add multiple elements to a list, then we can either use a for loop + list.append
# or we can use += 

# on a list, += runs a for loop on whatever is to our right

mylist = [10, 20, 30]
mylist += [40, 50, 60]   

mylist
# I can remove an element from the end with list.pop:

mylist.pop()
mylist
# I can also give list.pop an argument, the index I want to get rid of

mylist.pop(0)    # remove the first element, and everything else moves down one index
mylist
30 in mylist   # will this work?
# if I have a string, can I turn it into a list?

s = 'abcd'
list(s)    # I want a list, based on s
s = 'abcd:ef:ghij'   # this looks like several fields we want to separate
list(s)
# how can we deal with this?
# we can invoke the "str.split" method. It doesn't change the string (of course), but it does
# return a new list of strings:

s.split(':')   # this means: return a new list of strings, using ':' as the field separator, aka where to cut
s.split('d')   # weird, but it'll work!
s = 'abcd ef ghij'
s.split(' ')
s = 'abcd,ef,ghij'
s.split(',')
