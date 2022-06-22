# “Esercizio 1: Riscrivi lo script del calcolo della retribuzione per
# attribuire ad un dipendente una maggiorazione oraria di 1,5 volte,
# per le ore di lavoro straordinario fatte oltre le 40.”
#
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0


def payday(hours, rate, threshold=None):
    extra_pay = 0
    if threshold and hours > threshold:
        extra = hours - threshold
        hours = threshold
        extra_pay = extra * rate * 1.5
    return hours * rate + extra_pay


if __name__ == '__main__':
    rate = int(input('How much you pay your employee? '))
    pay = int(input('How many hours he worked? '))
    thrs = int(input('What\'s the amount of regular working hours? '))
    print(payday(pay, rate, thrs))
