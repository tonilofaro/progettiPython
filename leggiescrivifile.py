import os
f = open("testo.txt","r")
# print(f.read()) #legge tutto il file
# print(f.read(2)) # leggo i primi due caratteri
# print(f.readline()) # legge una riga del file
# print(f.readline()) # legge la seconda riga del file

for riga in f:
    print(riga)
f.close()


f = open("testo.txt","a") # append
f.write("ciao ")
f.close()

f = open("testo.txt","w") #sovrascrive
f.write("ciao sono andrea")
f.close()
print(os.cpu_count())

