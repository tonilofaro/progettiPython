x = {"milano","roma","napoli"}
y = {"milano",34,True}
print(len(x))
print(type(x))
y = set(("Torino","Padova","Milano")) # con il costruttore devo usare le parentesi tonde
# per accedere agli elementi posso usare solo il loop perchè non sono indicizzate i dati di un set non sono ordinati
for citta in x:
    print(citta) # ogni volta li stampa in ordine diverso

print("milano" in x) #check se esiste
# la modifica non si può fare
# per aggiungere
x.add("venezia")
print(x)
x.update(y) # aggiunge ad x gli elementi di y
print(x)
x.remove("Milano")  # se metto una città che non esiste remove da errore mentre discard no
x.discard("milano")
x.discard("londra") # non da errore se la città non esiste mentre remove si
print(x)
# x.pop toglie un elemento a caso
y = {"venezia","Udine","Milano"}

# la union andrà a creare un nuovo set
z = x.union(y)
print(z)
# sia union che update considerano i duplicati
x.intersection_update(z) # restiuisce solo gli elementi duplicati
print(x)
# per avere invece un nuovo set con solo elementi comuni
z = x.intersection({"roma","Torino","Udine"}) # escludo infatti Udine in quanto non presente in x
print(z)
# tiene tutto tranne i duplicati
z = x.symmetric_difference({"roma","Torino","Udine"})
print(z)
x.symmetric_difference_update(y)
print(x)