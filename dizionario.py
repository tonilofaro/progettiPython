persona = {
    "nome": "Andrea",
    "cognome": "Mazza",
    "anno_nascita": 1992,
    "luogo_nascita": "Torino"
}
chiave = input("inserisci chiave\n")
# if(chiave in persona):
print(persona.get(chiave, "chiave non valida"))  # equivale alla if
# print(persona[chiave])
# else:
# print("chiave non valida")
print(len(persona))
persona["coloriPreferiti"] = ["giallo", "rosso"]

for key in persona:
    print(key)  # stampa le chiavi

for valori in persona.values():
    print(valori)  # stampa i valori

for (key, value) in persona.items():
    print(key, value)
