# Esercizio 3: Scrivi un programma per richiedere un valore compreso
# tra 0.0 e 1.0. Se non è compreso nell'intervallo specificato, visualizza un messaggio di
# errore. Se è compreso tra 0,0 e 1,0, visualizza un giudizio utilizzando la seguente tabella:
# Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
#  < 0.6     F
# Enter score: 0.95
# A
# Enter score: perfect
# Bad score
# Enter score: 10.0
# Bad score
# Enter score: 0.75
# C
# Enter score: 0.5
# F

def score_to_grade(score):
    grade = 'A', 'B', 'C', 'D', 'F'
    if score < 0.6:
        return grade[4]
    elif score < 0.7:
        return grade[3]
    elif score < 0.8:
        return grade[2]
    elif score < 0.9:
        return grade[1]
    elif score <= 1.0:
        return grade[0]


while True:
    try:
        value = float(input('Enter score: '))
        if value > 1.0 or value < 0.0:
            raise ValueError
        else:
            print(score_to_grade(value))
    except ValueError:
        print('Bad score')
        continue
