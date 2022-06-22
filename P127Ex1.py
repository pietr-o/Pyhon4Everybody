# Write a function called chop that takes a list and modifies it,
# removing the first and last elements, and returns None. Then write a function
# called middle that takes a list and returns
# a new list that contains all but the first and last elements.”
#


def chop(t: list):
    del t[0]
    t.pop()
    return


def middle(t: list):
    last = len(t) - 1
    t2 = t[1:last]
    return t2


phrase = input('Input something: ')
converted = []
converted[:] = phrase
chop(converted)
print(*converted, sep='\n')
