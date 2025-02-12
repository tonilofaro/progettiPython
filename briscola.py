"""
Si scriva un programma Python che permetta di valutare il vincitore di una mano di una partita a Briscola tra due giocatori
Ipotizzare che il programma decida automaticamente ( in modo casuale) il "seme di briscola", e lo stampi come informazione iniziale.
il seme è codificato da una delle lettere C,Q,F,P.

I due utenti inseriscono poi ciascuno la carta giocata, sotto forma di stringa, che
contiene il valore seguito dal seme. I valori delle carte sono: A 2 3 4 5 6 7 J Q K. Il valore delle carte è crescente,
con l'eccezione del 3(che viene dopo il K) e dell'A(che viene dopo il 3).

Il primo giocatore gioca una carta, il cui seme definisce il seme della mano in gioco.
Il secondo giocatore può giocare una carta di un seme diverso(e quindi perde), oppure una carta dello stesso seme
( ed in tal caso vincerà quello che ha giocato la carta più alta).
Eccezione: le carte il cui seme è pari al seme della briscola vincono sempre sulle altre carte di ogni altro seme

Il programma, dopo aver stampato il seme della briscola scelto, accetterà la giocata del primo giocatore e del secondo giocatore.
Ogni giocata sarà quindi una stringa di due caratteri (es.:3Q,JF, ...).
Il programma accetterà sia lettere maiuscole che minuscole, e verificherà la correttezza del dato immesso.

Se i dati immessi sono corretti, il programma determinerà il vincitore della mano, stampando "Vince giocatore 1" oppure "Vince giocatore 2"

"""
from random import random, randint

SEMI = "CQFP"
VALORI = "24567JQK3A"  # metto l'elenco in ordine di valore della carta

# 1. Scegli e stampa il seme di briscola
# biscola = 'Q','C','F','P' codifico i semi con numeri da 0 a 3
# casuale = int(random()*4)  # genero un numero da 0 a 3  equivalente a quello di sotto

casuale = randint(0, 3)  # genera un numero casuale da 0 a 3
briscola = SEMI[casuale] # semi con indice quello generato casualmente
print(f'la biscola per questa mano è {briscola}')

# 2. Acquisisci e verifica la giocata 1
# definisce giocata 1 = '3F','JP', 2 caratteri maiuscoli di cui il primo tra VALORI  ed il secondo tra SEMI
# per prima cosa per buona norma definisco controlli minimali e poi andrò ad espandere i punti
giocata1 = input("Primo giocatore: ")
giocata1 = giocata1.upper().strip() # stringa maiuscola e senza spazi
if len(giocata1) != 2 or giocata1[0] not in VALORI or giocata1[1] not in SEMI:
    exit(f"Giocata {giocata1} non valida...")

# 3. Acquisisci e verifica la giocata 2
# definisce giocata 1 = '3F','JP', 2 caratteri maiuscoli di cui il primo tra VALORI  ed il secondo tra SEMI
giocata2 = input("Secondo giocatore: ")
giocata2 = giocata2.upper().strip()
if len(giocata2) != 2 or giocata2[0] not in VALORI or giocata2[1] not in SEMI:
    exit(f"Giocata {giocata2} non valida...")

if giocata1 == giocata2:
    exit("Giocata non valida perchè avete giocato le stesse carte")

# 4. Determina ie stampa il vincitore
# produce: il vincitore = (1 o 2)

print(f'avete giocato {giocata1} e {giocata2}')

# se uno ha giocato briscola e l'altro no, vince
if giocata1[1] == briscola and giocata2[1] != briscola:
    vincitore = 1
elif giocata2[1] == briscola and giocata1[1] != briscola:
    vincitore = 2
elif giocata1[1] != giocata2[1] and (giocata1[1] != briscola and giocata2 != briscola):
    # due semi diversi nessuno briscola, vince giocata 1
    vincitore = 1
else:
    # stesso seme(che sia briscola o no non importa)
    pos1 = VALORI.find(giocata1[0])  # l'indice del carattere
    pos2 = VALORI.find(giocata2[0])
    if pos1 > pos2:
        vincitore = 1
    else:
        vincitore = 2
print(f"Ha vinto il giocatore {vincitore}")
