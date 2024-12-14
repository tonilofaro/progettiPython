from pprint import pprint

NOME_FILE = 'elenco-comuni-italiani.csv'

comuni = []  # lista di tutti i comuni
comuni_per_codice = dict()  # dizionario vuoto usato come array associativo  da progressivo --> info comune
with open(NOME_FILE, 'r', encoding='utf-8') as f:
    f.readline()  # leggo la prima riga che contiene campi di intestazione
    for riga in f:
        campi = riga.rstrip('\n').split(';') # tolgo dove c'è l'acapo e divido dove trovo il ;
        comune = {
            'progressivo': int(campi[3].strip()), # tolgo lo spazio da questo campo e lo converto in intero
            'nome_comune': campi[6],   # il settimo campo letto dal csv è il nome del comune
            'nome_provincia': campi[11],
            'regione': campi[10]
        }
        comuni.append(comune)  # aggiungo alla lista i comuni che leggo
        comuni_per_codice[comune['progressivo']] = comune
     #   print(comune)


pprint(comuni)
pprint(comuni_per_codice)