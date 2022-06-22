# “Esercizio 2: Riscrivi lo script sul calcolo della retribuzione
# utilizzando try e except in modo che il programma gestisca input
# non-numerici in maniera elegante visualizzando un messaggio
# prima di uscire dal programma. Di seguito vengono mostrate due esecuzioni del programma:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input”

def payday(hours, rate, threshold=None):
    extra_pay = 0
    if threshold and hours > threshold:
        extra = hours - threshold
        hours = threshold
        extra_pay = extra * rate * 1.5
    return hours * rate + extra_pay


err_message = 'Error, please enter numeric input'
if __name__ == '__main__':
    while True:
        try:
            rate = int(input('How much you pay your employee? '))
        except ValueError:
            print(err_message)
            continue
        break
    while True:
        try:
            pay = int(input('How many hours he worked? '))
        except ValueError:
            print(err_message)
            continue
        break
    while True:
        try:
            thrs = int(input('What\'s the amount of regular working hours? '))
        except ValueError:
            print(err_message)
            continue
        break
    print(payday(pay, rate, thrs))
