citta = ["Milano", "Roma", "Torino"]
i = 0
while i < len(citta):  # cicla finchè la i è minore della lunghezza della lista
    print(citta[i])
    i += 1

i = 0
while i < len(citta):
    print(citta[i])
    if i == 1:  # si interrompe alla seconda iterazione
        break
    i += 1

# stampa solo numeri pari
i = 0
while i <= 10:
    if i % 2 != 0:
        i += 1
        continue
    print(i)
    i += 1
else:
    print("ho finito")

citta = ["Milano", "Roma", "Napoli", "Torino", "Empoli", "Genova", "Bardonecchia", "Bari", "Lucca"]
citta.append("Bitonto") # aggiunge un nuovo elemento in coda alla lista
for c in citta:
    print(c)   # ciclo for in ptython equale a un foreach
stringa = "Anguria"
for c in stringa:
    print(c)
for num in range(10): # range di numeri da 0 a 9
    print(num)


