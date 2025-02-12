# leggere del json che arriva



import json

# il json arriva come stringa
x = '{ "nome" : "luca","cognome" : "Nervi","eta" : 25 }'

y = json.loads(x) # crea un dictonary con l'oggetto json letto

print(y)

# Accesso ai dati del dizionario
print(y["nome"])  # Output: Luca
print(y["eta"])   # Output: 25

# da python  a json

persona = {
    "nome":"Andrea",
    "cognome":"Mazza",
    "eta": 30,
    "Anno_di_nascita": 1992,
    "indirizzo": {
        "via": "via po",
        "numero_civico": 1,
        "citta": "Torino"
    },
    "isOnline" : False ,
    "interessi" : ["calcio","basket"],
    "monetineIntasca" : 4.56,
    "fidanzata" : None
}

# Conversione in JSON
persona_json = json.dumps(persona,indent=4,sort_keys=True) # con indent posso renderlo più leggibile e sort_keyts ordina le chiavi in ordine alfabetico

print(persona_json)