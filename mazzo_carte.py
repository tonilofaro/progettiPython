# proviamo a gestire un mazzo di carte
# mazzo = ['7P','3F','AP'] # esempio
VALORI = "2456JQK3A"
SEMI = "PFQC"

VALORI = ['2', '4', '5', '6', 'J', 'Q', 'K', '3', 'A']


# converti una lista di stringhe in una lista di numeri
# [ '2','4','5','7'] --> [2,4,6,7]

# modifica la lista parametro
def str_to_int(valori):
    for i in range(len(valori)):
        valori[i] = int(valori[i])


# non modifica il parametro , restituisce una nuova lista

def nuova_str_to_int(valori):
    nuova = []
    for v in valori:
        nuova.append(int(v))
    return nuova



dati = ['2', '4', '5', '7']
print(dati)
str_to_int(dati)
print(dati)
dati = ['2', '4', '5']
print(dati)
nuovalista = nuova_str_to_int(dati)
print(nuovalista)

