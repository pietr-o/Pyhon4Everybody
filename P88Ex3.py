# Exercise 3: Encapsulate this code in a function named count,
# and generalize it so that it accepts the string and the letter as arguments.

def count(word=int | str):
    index = 0
    for letter in word.lower():
        if letter == 'a':
            index += 1
    print(f'Found %d "a" characters' % index)


buffer = input("Write something with 'a's inside: ")
count(buffer)
