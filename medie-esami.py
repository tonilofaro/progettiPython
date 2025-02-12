"""
1) chiedi quanti esami devono essere considerati per ciascun studente
memorizzalo in n_esami , che deve essere un valore intero >= 1
"""
n_esami = int(input("Quanti esami ci sono?"))
while n_esami < 1:
    print("valore non valido")
    n_esami = int(input("Quanti esami ci sono?"))

"""
2) acquisisci i voti e calcola le medie
ripetere per ciascun studente
variabile di controllo: 'ancora' Booleano oppure
Variabile di controllo: stringa 'S' o 'N'
"""
ancora = True
while ancora:
    # 2.1) leggi i suoi voti
    # 2.1.0) inizializza somma_voti a 0
    print("inserisci i voti dello studente")
    somma_voti = 0
    # RIPETI PER n_esami volte
    #    2.1.1) leggi un voto
    #    2.1.2) aggiorna somma voti

    for i in range(n_esami):
        voto = int(input(f"Voto numero {i + 1} = "))
        while voto < 18 or voto > 30:
            print("Voto errato")
            voto = int(input(f"Voto numero {i + 1} = "))
        somma_voti = somma_voti + voto

    #  2.2) calcola e stampa la media
    #  somma_voti / n_esami
    media = somma_voti / n_esami
    print(f"La media è: {media}")

    #  2.3) chiedi se ci sono altri studenti da elaborare
    #  aggiorna ancora
    risposta = input("ci sono ancora studenti? (S/N)").upper().strip()
    while risposta != 'S' and risposta != 'N':  # risposta in 'SN' alternativa
        risposta = input("ci sono ancora studenti? (S/N)").upper().strip()

    if risposta == 'S':
        ancora = True
    else:
        ancora = False
#  2.3) chiedi se ci sono altri studenti da elaborare
#    aggiorna ancora

"""




"""
