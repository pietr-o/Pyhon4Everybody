# Minimalistic email client

mbox = open('./TXT/mbox.txt')
mail_count = 0
for line in mbox:
    if line.startswith('From '):
        words = line.split()
        mail_count += 1
        print(words[1])
print(f'*************************'
      f'\nThere were %d lines in the file with "From " as the first word"'% mail_count)