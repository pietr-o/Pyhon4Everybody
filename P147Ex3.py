mbox = open('./TXT/mbox.txt')
count = 0
day = {}
for line in mbox:
    if not line.startswith('From '): continue
    count += 1
    line = line.split()
    day[line[1]] = day.get(line[1], 0) + 1
for d, c in day.items():
    print('-'*c, '*')
    print(f'{d}\t{c}')
