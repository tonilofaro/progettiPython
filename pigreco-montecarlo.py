# decido quanti punti casuali generare : n_punti
import random

n_punti = int(input('Numero di punti: '))
n_interni = 0
# Ripeto per n_punti volte
for i in range(n_punti):
    # Genera le coordinate (x,y) casuali nel range [-1,+1]
    x = random.random()*2.0 - 1.0
    y = random.uniform(-1.0,1.0) # da un valore causale da -1 a 1
    # verifica se il punto cade all'interno del cerchio
    # aggiornando il n_interni
    if x*x + y*y <= 1.0:
        n_interni += 1
# fai i calcoli
area_quadrato = 4.0
area_cerchio = area_quadrato * (n_interni/n_punti)
print(f'P greco vale {area_cerchio}')