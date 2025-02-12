"""
partendo da un capitale iniziale di 10000 euro, quanti anni sono necessari per raddoppiare il capitale , se esso viene
investito con un interesse fisso scomposto pari al 5%?
"""
capitale_iniziale = 10000
capitale_finale = capitale_iniziale * 2
tasso_interesse = 0.05
capitale = capitale_iniziale
anni = 0
while capitale < capitale_finale:
    interesse = capitale * tasso_interesse
    capitale = capitale + interesse
    anni = anni + 1

print(f"Hai raggiunto il capitale di {capitale} euro in {anni} anni")