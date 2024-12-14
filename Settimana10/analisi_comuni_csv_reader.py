import operator
from pprint import pprint
from csv import DictReader

NOME_FILE = 'elenco-comuni-italiani.csv'

comuni = []  # lista di tutti i comuni
comuni_per_codice = dict()  # dizionario vuoto usato come array associativo  da progressivo --> info comune
with open(NOME_FILE, 'r', encoding='utf-8') as f:
    reader = DictReader(f,delimiter=';')  # legge già il file facendo lui le split e togliendo l'acapo dobbiamo dirgli che il ; è il separatore , posso anche personalizzare il nome delle chiavi
    for record in reader:
        comuni.append(record)  # record è già un dizionario

#comuni.sort(key=lambda record: record['Denominazione in italiano'])  # funziona anonima  rinomina per denominazione in italiano

comuni.sort(key=operator.itemgetter('Denominazione in italiano'))  # analogo a quello di sopra ma usando itemgetter
pprint(comuni)