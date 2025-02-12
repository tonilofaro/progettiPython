"""
Testa o croce
Sviluppare un programma per permettere ad un utente di giocare una partita a "testa o croce"
L'utente dovrà inizialmente inserire il proprio tentativo, inserendo un carattere 'T' o 'C'.
il programma in seguito simulerà casualmente il lancio della moneta, determinando se è uscito 'T' o 'C'
Infine, sulla base del valore estratto, il programma comunicherà all'utente se ho vinto o perso.

"""
import random

# 1 leggi il tentativo dell'utente
# Output di questa fase: variabile: tentativo 'T' oppure 'C'
tentativo = input("Cosa uscirà (T/C)? ")
tentativo = tentativo.strip().upper() # ripulire gli spazi e mettere in maiuscolo

# controlla che sia T oppure c altrimenti fermati


# 2. Simula il lancio della moneta
# Output di questa fase: varaibile: moneta 'T' oppure 'C'

caso = random.random() # genera un valore da 0 a 1
if caso < 0.5:
    moneta = 'T'
else:
    moneta = 'C'


# 3. determinare se l'utente ha vinto

print('Tentativo =', tentativo, 'Moneta =', moneta)
if tentativo == moneta:
    print("hai vinto!")
else:
    print("hai perso!")
