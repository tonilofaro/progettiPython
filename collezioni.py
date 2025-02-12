# creazione lista con già dei valori presenti
citta = ["Milano", "Roma", "Napoli", "Torino", "Empoli", "Genova", "Bardonecchia", "Bari", "Lucca"]


# Le liste sono collezioni ordinate e modificabili. Permettono duplicati

# funzione
def saluta():
    return "ciao"

def somma(a, b):
    return a + b

print(saluta())
print("la somma è", somma(3, 4))

cittaFrancesi = list() # creo una lista vuota oppure tra parentesi tonde posso metterci gli elementi
cittaFrancesi.append("Parigi") # aggiungo alla posizione 0 Parigi
print(cittaFrancesi[0:])
cittaFrancesi[0] = "Lione" # modifico l'elemento
cittaFrancesi.append("Bordeaux")
print(cittaFrancesi[:]) # due punti indica un range e mettendo così stampa tuto
citta[0:2] = ["Brescia","Cagliari"] # MODIFICO elemento 0 e 1
print(citta[:])
citta.append("Loano") # inserisce in fondo
print(citta[:])
citta.insert(1, "Venezia") # inserisce l'elemento all'indice indicato
print(citta)
citta.extend(cittaFrancesi) # estende gli elementi di una lista concatenando gli elemnti di un altra lista
print(citta)
citta.remove("Cagliari")
citta.pop() # rimuove l'elemento in fondo, posso anche specificare un indice
del citta[0] # cancella l'elemto 0
print(citta)
for x in citta:
    print(f"la città è {x}")

[print(c) for c in cittaFrancesi if c != "Lione"] # list comprehesion
citta.sort() # ordina la lista
print(citta)
citta.sort(reverse=True) # ordina al contrario
print(citta)
citta2 = citta.copy() # copia della lista
citta3 = list(citta) # copia della lista
citta.clear() # cancella tutti gli elementi della lista
print(citta)
del citta # cancella proprio la lista
print(citta2)
cittaTot = citta2 + citta3  # unire più liste. si può anche usare append mettendo più elementi dentro oppure extend
print(cittaTot)
