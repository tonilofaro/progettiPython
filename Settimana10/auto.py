from pprint import pprint


def leggi_auto(nome_file):
    f = open(nome_file,'r',encoding='utf-8')
    #scarto la prima linea perchè contiene l'intestazione
    f.readline()
    auto = []   # lista auto
    for riga in f:
        #estraggo i campi di ogni riga riga conterrà:  utilitaria,FIAT,Panda,rosso,L,L,L,A,A,A,A esempio
        # tolgo a capo e splitto dove c'è la virgola
        campi = riga.rstrip('\n').split(',') # facendo split mi restituisce una lista con all'interno tutti i campi
        # print(campi)
        record = {
            'categoria': campi[0],
            'marca': campi[1],
            'modello': campi[2],
            'colore': campi[3],
            'disponibile': campi[4:11] #indice metto 11 anche se gli elementi sono 10
        }
        auto.append(record) # aggiungo alla lista di auto
    f.close()
    return auto


def ricerca_auto(auto, categoria, giorni):
    disponibili = []
    for veicolo in auto:
        if veicolo['categoria'] == categoria:  #categoria ok controllo i giorni
            ok = True
            for g in giorni: #ricerco ogni giorno da quelli inseriti in input
                #veicolo disponibile è la lista gli do indice g che sono i giorni
                if veicolo['disponibile'][g-1] != 'L':  # -1 perchè i giorni vanno da 1 a 7 mentre gli indici da 0 a 6
                    ok = False
            if ok: # se alla fine ho trovato la disponibilità aggiungo
                disponibili.append(veicolo)
    return disponibili


def main():
    auto = leggi_auto('auto.csv')
    # pprint(auto)
    richiesta = input('scegli categoria e giorni: ')
    campi_richiesta = richiesta.split()
    categoria_richiesta = campi_richiesta[0]
    giorni_richiesti = [int(c) for c in campi_richiesta[1:] ] # converto in intero perchè altrimenti avtei una stringa
    # cerco le auto disponibili sulla base degli input dati
    auto_disponibili = ricerca_auto(auto,categoria_richiesta,giorni_richiesti)
    if len(auto_disponibili) == 0:
        print("non ho trovato nessuna auto disponibile")
    elif len(auto_disponibili) == 1:
        auto_scelta = auto_disponibili[0]
        print(f'1) {auto_scelta["marca"]} {auto_scelta["modello"]} colore {auto_scelta["colore"]}')
        for g in giorni_richiesti:
            auto_scelta['disponibile'][g-1] = 'A'  # va a modificare direttamente la lista delle auto principale
    else:
        print('le auto disponibili sono: ')
        for indice,macchina in enumerate(auto_disponibili):
            print(f'{indice+1}) {macchina["marca"]} {macchina["modello"]} colore {macchina["colore"]}')
        prenotare = int(input('quale vuoi prenotare?'))
        auto_scelta = auto_disponibili[prenotare-1]
        for g in giorni_richiesti:
            auto_scelta['disponibile'][g-1] = 'A'

    for veicolo in auto:
        print(f'{veicolo["categoria"]},{veicolo["marca"]},{veicolo["modello"]},{veicolo["colore"]},',end='')
        print(','.join(veicolo['disponibile']))






main()