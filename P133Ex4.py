fhand = open('./TXT/romeo.txt')
word_list = {}
for line in fhand:
    for word in line.split():
        if len(word) != 0: word_list[word] = word_list.get(word,0) + 1
sorted_list = [(k, v) for k, v in word_list.items()]
sorted_list.sort()
print('|#|\tValue')
for k, v in sorted_list:
    print(f'|{v}|\t{k}')

