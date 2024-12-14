FILE_POPOLAZIONE = 'worldpop.txt'
FILE_AREA = 'worldarea.txt'
FILE_DENSITA = 'world_pop_density.txt'


def separa(riga):
    riga = riga.rstrip('\n') # tolgo a capo
    campi = riga.rsplit(maxsplit=1) # partendo da destra massimo 1 splitta mi da una lista massimo di due elementi
    nazione = campi[0]
    valore = int(campi[1])
    return nazione, valore


f_pop = open(FILE_POPOLAZIONE, 'r', encoding='utf-8')  # leggo i file in lettura
f_area = open(FILE_AREA, 'r', encoding='utf-8')
f_densita = open(FILE_DENSITA, 'w', encoding='utf-8') # leggo il file in scrittura


# leggo la prima riga dal primo e dal secondo file
riga_pop = f_pop.readline()
riga_area = f_area.readline()

# ciclo fino alla fine dei file
while riga_pop!='' and riga_area!='':

    # elabora
    # print(riga_pop)
    # print(riga_area)

    # funzione che legge la riga intera e me la separa in due valori distinti
    nazione1, popolazione = separa(riga_pop)
    nazione2, area = separa(riga_area)

    if nazione1==nazione2:  # controllo se le due nazioni esistono
        if area!=0:
            densita = popolazione/area
            print(nazione1, f'{densita:.2f}', file=f_densita) # scrive l'output sul file prendendo massimo due cifre decimali
        else:
            print(nazione1, 'n.d.', file=f_densita)

    else:
        exit("File non sincronizzati")

    #leggo le righe successive dopo aver fatto l'elaborazione
    riga_pop = f_pop.readline()
    riga_area = f_area.readline()


f_pop.close()
f_area.close()
f_densita.close()
