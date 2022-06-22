# This program stores a list of inputs from the user and prints out the minimum and maximum

store = []
count = 0
while True:
    count += 1
    d = input(f'{count}) ')
    if d.lower() == 'q': quit(2)
    if d.lower() == 'e': break
    try:
        d = int(d)
        store.append(d)
    except ValueError:
        print(f'%s is not a number' % d)
        continue
print('The maximum of your input is: ', max(store))
print('The minimum of your list is: ', min(store))
print('*' * 20, '\nHere\'s a simple graph')
count = 0
for i in store:
    count += 1
    if i < 150:
        representation = '-' * i
    else:
        representation = ('-' * 75) + ' [...] ' + ('-' * 75)
    print(f'%d|%s> %d' % (count, representation, i))
