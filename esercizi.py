# prende in input un messaggio

# messaggio = input("inserisci qualcosa:")
# print(messaggio)
if 1 < 5:
    print("nell'if")
else:
    print("mai stampato")
print("fuori if")
a, b, c = 3.2, 4, 5  # assegnazione multipla di variabili
x = y = z = 4  # x ,y e z assumono tutti e 3 il valore 4
print("calcola totale variabili: ", a + b + c + x + y + z)

# intero
numero = 5
print(type(numero))  # mi dice di che tipo è la variabile
# stringa
parola = "ciao"
# float
numero_virgola = 6.43
# booleano
isName = True
# lista
citta = ["roma", "milano", "torino"]
# tuple
citta = ("roma", "napoli", "milano")
# range
my_range = range(6)  # genera un array da 0 a 6 contenente numeri da 0 a 6
print(my_range[0], my_range[1], my_range[2])
# dizionario
x = {"nome": "Luca", "cognome": "alone", "eta": 32}
# set
y = {"roma", "luca", "hotel"}
multiLineaStringa = """ciao 
sono andrea e abito a 
torino
"""
print(multiLineaStringa)
print(parola[0])  # stampa la prima lettera
print(len("sono"))  # lunghezza della stringa
print(parola[:2])  # stampa dall'inizio al carattere 2
print(multiLineaStringa[0:3])  # dal primo al terzo carattere
print(multiLineaStringa.upper())
print(multiLineaStringa.strip())  # toglie gli spazi in eccesso
print(multiLineaStringa.replace("ciao", "addio"))  # sostiuisce le occorrenzw di ciao con addio
z = parola + "ANDREA"
print(z)

giorno = 19
prova = "ciao sono andrea e sono nato il {0} e sono alto {1}"  # interpreta le parentesi come contenitore di una variabile numerica, indici di format
print(prova.format(giorno, 183))  # sostuisce in ordine di come trova le parentesi

# escape
prova = "ciao sono andrea e sono \"figo\" "
print(prova)

# booleani
x = True
y = False
print(5 < 10)
if (x):  # condizione sempre vera in questo caso
    print("LOAH")

print(bool(0))  # valuto un valore 0 da false
print(bool(""))

lista_cose_da_comprare = []
if lista_cose_da_comprare:  # valutare così un'espressione
    print("andare al supermercato")
else:
    print("lista vuota niente da compare")

x = 10
if x == 10:
    print("verità assoluta")

if x != 9:
    print("x diverso da 9")
elif x < 9:
    print("ciao")
else:
    print("addio")

x = 16
if 10 < x < 20:  # python accetta la sintassi del compreso come matematica
    print("x compreso tra 10 e 20")
if x > 10 and x < 20:
    print("x compreso tra 10 e 20")  # stessa cosa di quello di sopra
if x > 10 or x == 30:
    print("fai qualcosa")  # sintassi or comprende proprio la parola "or" non le doppie barre
if not (x < 10):  # not nega la condizione
    print("condizione verificata")

# versione short di if

if x > 10: print("è maggiore di 10")  # si può fare solo se abbiamo un'istruzione dopo

if x > 10:
    if x % 2 == 0:
        print("numero pari maggiore di 10")
    else:
        print("numero dispari maggiore di 10")
else:
    print("numero <= 10")

parola = "superman"
print(parola[::2])  # stampa caratteri pari
print(parola[1::2])  # stampa caratteri dispari
print(parola[::-1]) # fa il revert della stringa
print(parola.replace("man", "woman")) # sostuisce l'occorenza di man con woman

s = input("inserisci qualcosa:\n") # input accetta solo stringhe
print(s)
numeroMagico = int(input("inserisci il numero magico: ")) # se inserisco un numero devo convertirlo in un numero
print("il numero magico è:",numeroMagico)

print(f"ciao sono {numeroMagico} mentre lui è {parola[1]}") # format