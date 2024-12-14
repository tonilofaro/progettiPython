from pprint import pprint

FILE_COMUNI = 'elenco-comuni-italiani.csv'

f = open(FILE_COMUNI, 'r', encoding='utf-8')

_ = f.readline() # leggo la prima riga che non serve

nomi_comuni = []

for riga in f:
    campi = riga.rstrip('\n').split(';')  # ogni campo che legge è una lista
    nome_comune = campi[6]  # la settima colonna è il nome del comune italiano
    nomi_comuni.append(nome_comune)

nomi_comuni.sort() # ordina

# pprint(nomi_comuni)

for nome in nomi_comuni:
    print(nome)

f.close()
