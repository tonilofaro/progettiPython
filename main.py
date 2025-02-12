import voto

print("ciao", 3+2)
variabile = 1
print(variabile)
variabile = 2
print(variabile)

voto_1 = voto.Voto("matematica",10,25,False,'2021-05-10')
voto_2 = voto.Voto("matematica",10,22,False,'2024-05-14')

librettino = voto.Libretto()

librettino.append(voto_1)
librettino.append(voto_2)

print(librettino.media())

try:
    print(x)
except NameError:
    print("x non definita")
except BaseException:
    print("altro")
else:
    print("nessun problema")
finally:
    print("chiudo connessione al db o chiudo il file")
   # raise FileNotFoundError  lancio io un eccezione


persona = {
    "nome" : "Luca",
    "cognome": "Rossi",
    "eta": 27
}

operazioni = ("aggiungere","modificare","eliminare","terminare","stampa")


def aggiungi(param):
    chiave = param[0]
    valore = param[1]
    persona[chiave] = valore


def stampa():
    print(persona)


def start():
    operazione = input("Cosa vuoi fare?\n")
    if operazione == operazioni[0]:
        c = input("aggiungi chiave: valore separati da una virgola\n")
        aggiungi(c.split(","))
    elif operazione == operazioni[1]:
        pass
    elif operazione == operazioni[2]:
        pass
    elif operazione == operazioni[3]:
        exit()
    elif operazione == operazioni[4]:
        stampa()

#while True:
    # start()

altezza = 183
peso = 79
nome = "Andrea"

frase = f"ciao sono {nome} , sono alto {altezza} cm e peso {peso} kg "

frase2 = "Ciao sono {0} sono alto {1:.2f} cm  e peso {2} kg"

print(frase)

print(frase2.format(nome,altezza,peso))



