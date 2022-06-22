line = 'X-DSPAM-Confidence:0.8475'
char_pos = line.rstrip().find(':')
value = line[char_pos + 1:]
try:
    print(float(value))
except ValueError:
    print("Value not found or not valid")
