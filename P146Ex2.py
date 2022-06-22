# “Exercise 2: Write a program that categorizes each mail message by which day
# of the week the commit was done. To do this look for lines that start with "From",
# then look for the third word and keep a running count of each of the days of the week.
# At the end of the program print out the contents of your dictionary (order does not matter).”

mbox = open('./TXT/mbox.txt')
count = 0
day = {}
for line in mbox:
    if not line.startswith('From '): continue
    count += 1
    line = line.split()
    day[line[2]] = day.get(line[2], 0) + 1
for d, c in day.items():
    print(f'{d}\t{c}')
