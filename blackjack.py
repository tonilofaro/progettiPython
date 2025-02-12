"""
realizzare un algoritmo e scrivere un programma python che giochi a blackjack con l'utente
Si assuma che la mano si svolga tra il banco e un solo giocatore
L'obiettivo del blackjack è di avere in mano delle carte la cui somma sia più vicina a 21, ma senza superarlo
è necessario tenere traccia della somma delle carte che i due giocatori (banco e giocatore) ricdevono durante la mano)
"""
import random


def leggi_conferma():
    risposta = input("Vuoi un'altra carta? (s/n) ")
    risposta = risposta.strip().lower()
    while risposta != 's' and risposta != 'n':
        print("valore errato")
        risposta = input("Vuoi un'altra carta? (s/n) ")
        risposta = risposta.strip().lower()
    return risposta


print("PARTITA A BLACK JACK")
# computer si dà una carta
# salva in un 'carta_computer'
carta_computer = random.randint(1, 10)
print(f"il computer ha estratto un {carta_computer}")

# computer da due carte al giocatore
# Facciamo giocare il giocatore
# (finchè decide di fermarsi oppure supera 21)
# determina variabile 'punti_giocatore'

carta_giocatore_1 = random.randint(1, 10)
carta_giocatore_2 = random.randint(1, 10)
punti_giocatore = carta_giocatore_1 + carta_giocatore_2
print(f"le tue carte sono {carta_giocatore_1} e {carta_giocatore_2}")
risposta = leggi_conferma()
while risposta == 's' and punti_giocatore < 21:
    carta_giocatore = random.randint(1, 10)
    print(f"è uscito un {carta_giocatore}")
    punti_giocatore = punti_giocatore + carta_giocatore
    if punti_giocatore > 21:
        print("Hai superato 21")
    elif punti_giocatore == 21:
        print("Complimenti, hai raggiunto 21")
    else:
        risposta = leggi_conferma()

# facciamo giocare il computer ( strategia da definire)
# partendo dalla 'carta_computer' già estratta
# (finchè "decide" di fermarsi oppure supera 21)
# determina variabile 'punti_computer'
punti_computer = carta_computer
if punti_giocatore > 21:
    print("passo")
else:
    # ipotesi il computer può vedere tutte le carte del giocatore
    while punti_computer < punti_giocatore and punti_computer < 21:
        carta_computer = random.randint(1, 10)
        print(f"ho estratto un {carta_computer}")
        punti_computer += carta_computer
        if punti_computer > 21:
            print("Ho superato il 21")
    # ipotesi: il computer non può vedere le carte del giocatore, e mira a raggiungere il 17
    # modificare così:
    # while punti_computer < 17 and punti_computer < 21:

# verifica chi ha vinto
# sulla base di punti_giocatore e punti_computer
print(f"Punti giocatore = {punti_giocatore}, punti computer = {punti_computer}")
if punti_giocatore > 21:
    print("Hai perso")
elif punti_computer > 21:
    print("Hai vinto")
elif punti_giocatore > punti_computer:
    print("Hai vinto")
else:
    print("Hai perso")
