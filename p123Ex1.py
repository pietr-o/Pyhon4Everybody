# Esercizio 1: Scrivi un programma che legga ripetutamente i numeri fino a quando
# l'utente non digiti "finito". Una volta che viene digitato "finito",
# dovrà essere visualizzato il totale, il conteggio e la media dei numeri.
# Se l'utente dovesse digitare qualcosa di diverso da un numero, occorrerà rilevare l'errore usando try e except,
# visualizzare un messaggio di errore e passare al numero successivo.
import statistics

handbook = list()
while True:
    buff = input('Enter a number: ')
    if buff == 'done':
        break
    try:
        buff = float(buff)
        handbook.append(buff)
    except ValueError:
        print('Bad data. Value ignored.')
        continue
print(f"Items count: {len(handbook)}, Sum: {sum(handbook)}, Average: {statistics.mean(handbook)}")


