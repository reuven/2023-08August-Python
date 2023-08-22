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
