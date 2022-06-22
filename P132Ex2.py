fhand = open('./TXT/mbox-short_debug.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0] != 'From': continue
    if len(words) >= 3: print(words[2])
