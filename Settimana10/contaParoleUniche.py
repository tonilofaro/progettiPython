TESTO = "mary.txt"
parole_uniche = set()
frequenza_parole = dict()

with open(TESTO, 'r', encoding='utf-8') as f:
    for riga in f:
        parole = riga.rstrip('\n').split()
        for i in range(len(parole)):
            parole[i] = parole[i].lower().strip('.,"?;')
        parole_uniche = parole_uniche.union(set(parole))

        for parola in parole:
            if parola in frequenza_parole:  #se la parola è già presente tra le chiavi dove registro le parole devo solo incrementare la frequenza se no devo inserire la chiave
                frequenza_parole[parola] = frequenza_parole[parola] + 1
            else: # prima volta la creo
                frequenza_parole[parola] = 1




print(f'Le parole uniche presenti sono {len(parole_uniche)}')

print("frequnza parole:")
# print(frequenza_parole)

for parola,frequenza in sorted(frequenza_parole.items()):
    print(f'{parola:15s} {frequenza:2d}')
