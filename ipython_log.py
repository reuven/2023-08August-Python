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
