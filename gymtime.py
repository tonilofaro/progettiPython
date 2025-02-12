"""
leggere da tastiera una serie di numeri interi positivi, terminando l'inserimento con il valore -1, e stampando la loro somma

mi devo chiedere:
1. qual è l'operazione da ripetere? Lettura del numero
2. qual è la condizione per cui il ciclo va ripetuto?
3. inizializzazione della somma
4. inizializzazione della variabile del ciclo
"""
# variante 1
# somma = 0
# num = 0  # valore inizale fasullo
# while num != -1:
# num = int(input("leggi un numero: "))
# if num >= 0:
# somma = somma + num

# print(f"la somma è: {somma}")

# variante 2:

"""
somma = 0
num = 0
ok = True
while ok:
    num = int(input("leggi un numero: "))
    if num == -1:
        ok = False
    else:
        somma = somma + num

print(f"la somma è: {somma}")
"""
"""
somma = 0
num = int(input("leggi un numero: "))
while num != -1:
    somma += num
    num = int(input("leggi un numero: "))

print(f"la somma è: {somma}")

"""

# variante 1: termina se inserisco uno spazio
"""
somma = 0
riga = input("leggi un numero: ").strip()
while riga != '':
    num = int(riga)
    somma += num
    riga = input("leggi un numero: ").strip()

print(f"la somma è: {somma}")

"""
"""
# variante 2: estensione se il valore non è valido ad esempio negativo , richiederlo

somma = 0
riga = input("leggi un numero: ").strip()
while riga != '':
    num = int(riga)
    
    while num < 0:
        riga = input("leggi un numero: ").strip()
        num = int(riga)
        #TODO se l'utente inserisce '' dopo un numero negativo, il programma dà errore

    somma += num
    riga = input("leggi un numero: ").strip()

print(f"la somma è: {somma}")
"""
# variante 3: se il valore inserito non è valido(ad esempio negsativo),ignorarlo

somma = 0
trovato = False
riga = input("leggi un numero: ").strip()
while riga != '':
    num = int(riga)
    if num >= 0:
        somma += num
        if num % 3 == 0:
            trovato = True
    riga = input("leggi un numero: ").strip()

# alla fine del ciclo, dire se sono stati inseriti dei multipli di 3
print(f"la somma è: {somma}")
if trovato:
    print("è stato trovato almeno un multiplo di 3")
