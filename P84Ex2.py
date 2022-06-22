import statistics


def extract_confidence(string: str):
    string = string.replace(' ', '')
    pos = string.find(':')
    return float(string[pos + 1:])


root = './TXT/'
while True:
    filename = input('Enter a filename: ')
    if filename == 'na na boo boo':
        print('NA NA BOO OO TO YOU! - You\'ve been punk\'d!')
        continue
    if filename.endswith('.txt'):
        ext = ''
    else:
        ext = '.txt'
    path = root + filename + ext
    try:
        fhand = open(path)
        break
    except FileNotFoundError:
        print('Filename not found')
        continue
rows = 0
values_spam_confidence = []
for line in fhand:
    rows += 1
    if line.lstrip().upper().startswith('X-DSPAM-CONFIDENCE:'):
        values_spam_confidence.append(extract_confidence(line))
if values_spam_confidence:
    print('Average spam confidence: ', statistics.mean(values_spam_confidence))
    print(f'Compared %d values' % len(values_spam_confidence))
else: print('Not found')
print(f'Read %d lines' % rows)
answer = input('Would you like to see the whole list? (y/N) ')
match answer:
    case 'y': show_list = True
    case _: show_list = False
if show_list:
    cnt = 0
    for val in values_spam_confidence:
        print(f'#%d - %s' % (cnt, val))
        cnt += 1
else:
    print('Thank you!')
