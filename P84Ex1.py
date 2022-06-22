filename = input('Enter a filename: ')
root = './TXT/'
if filename.endswith('.txt'):
    ext = None
else:
    ext = '.txt'
path = root + filename + ext
print(path)
try:
    fhand = open(path)
except FileNotFoundError:
    print('Filename not found')
    exit(2)
rows = 0
for line in fhand:
    print(line.upper().rstrip())
    rows += 1
print(f'Read %d lines' % rows)
