# Exercise 1: Write a while loop that starts at the last character
# in the string and works its way backwards to the first character
# in the string, printing each letter on a separate line, except backwards.
reverse_me = input('Input string: ')
print('Your string is: %s' % reverse_me)
while reverse_me:
    for count in range(len(reverse_me)):
        print(f'{count}) {reverse_me[len(reverse_me) - count - 1]}')
    quit(0)
