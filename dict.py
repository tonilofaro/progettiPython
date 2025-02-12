# i dictonary sono gli equivalenti degli oggetti javascript
# non ammette chiavi duplicate
persona = {
    "nome":"Andrea",
    "cognome":"Mazza",
    "eta": 30,
    "Anno_di_nascita": 1992
}
print(persona)

# accesso a un elemento
print(persona["nome"])
print(persona.get("cognome"))

# prendo tutte le chiavi: e restituisce una lista
print(persona.keys())
# prendo solo i valori
print(persona.values())
# lista di duple con item chiave valore
print(persona.items())

#modificare un elemento
persona["eta"] = 31
print(persona)
# alternativa:
persona.update({"nome":"Marco"})
print(persona)
# aggiungere un elemento:
persona["colore"] = "blu"
print(persona)
# rimuovere l'elemento:
persona.pop("colore")
persona.popitem() # rimuove l'ultimo item presente
print(persona)
del persona["nome"] # cancella nome
print(persona)

# stampa le chiavi
for x in persona:
    print(x)

# cicla i valori
for x in persona:
    print(persona[x])

# oppure analogalmente alla precedente
for x in persona.values():
    print(x)
# copia del dizionario
x = persona.copy()

# dict annidati
persona = {
    "nome":"Andrea",
    "cognome":"Mazza",
    "eta": 30,
    "Anno_di_nascita": 1992,
    "indirizzo": {
        "via": "via po",
        "numero_civico": 1,
        "citta": "Torino"
    }
}
print(persona)
print(persona["indirizzo"]["citta"])
