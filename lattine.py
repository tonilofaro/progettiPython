# dati:
# una lattina contiene 12 once
# 12 oncie = 0.355 litri
# qual è la capacità totale di 6 lattine?
# sarà più o meno di 2 litri?
# capacità in once = 12
# numero di lattine = 6
# fattore di conversione once -> litri = 0.355 / 12
# capacità di una lattina in litri è uguale a capacità in once * fattore di conversione once -> litri

# capacità totale = capacità numero lattina per numero di lattine( in litri)
from math import sqrt, log  # importo la liberia
import cmath  #posso anche importare il modulo
capacita_lattina = 12  # once
numero_lattine = 6
CONVERSIONE_ONCE_LITRI = 0.355 / 12
capacita_lattina_litri = capacita_lattina * CONVERSIONE_ONCE_LITRI
capacita_tot = capacita_lattina_litri * numero_lattine

print("la capacità totale di 6 lattine è:", capacita_tot, "litri")

nome = "Andrea"
cognome = "Mazza"
print("mi chiamo", nome + " " + cognome)
print("esempio di potenza di 2 elevato 3:", 2 ** 3)
print("divisione considerando parte decimale:", 4 / 2)
print("divisione ignorando parte decimale:", 4 // 2)
if 4 % 2 == 0:
    print("ok")
print(abs(-345))  # valore assoluto
print(max(4, 3, 5, 2, 3, 4, 56, 7))
print(min(3, 4, 1, 5))
print(int(sqrt(4)))  # radice quadrata la forzo ad essere intero
print(round(log(4), 2))
print(cmath.sin(2))
print(len("ciao"))
print("ciao" * 4)