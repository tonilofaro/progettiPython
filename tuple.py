# tuple
x = ("Milano","Roma","Napoli")
y = ("Milano",True,45)
z = ("Torino")
print(type(x))
print(type(z)) # mi dice che è una stringa perchè per avere una tupla di un solo valore bisogna mettere una virgola
z = ("Torino",)
print(type(z))
print(len(x))
z = tuple(("Milano","Roma")) # uso il costruttore
print(z)
print(z[0]) # per accedere agli elementi si usa la sintassi come la lista
# verificare che l'elemento esiste
if "Milano" in x:
    print(f"esiste Milano in x")
# non è possibile modificare gli elmenti: x[0] = "Venezia" ad esempio non è consentito
y = list(x) # creo una lista derivante dalla tupla x
print(y)
y[0] = "Venezia" # sulle liste la modifica è consentita
print(y)
y.remove("Venezia")
y.append("Torino")
x = tuple(y) # x diventa una tupla di y
print(x) #escamotage per modificare una tupla

#spacchettare una tupla:
(citta1,citta2,citta3) = x
print(citta1)
print(citta2)
print(citta3)
# per ciclARE gli elementi usare il for

# unire le tuple
y = x + z
print(y)
print(y.count("Torino")) # conta quante volte è presente un elemento
