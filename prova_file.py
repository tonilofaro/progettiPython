f = open("storia.txt", "r", encoding='utf-8')
g = open("storia_big.txt", "w", encoding='utf-8')
# legge tutto il contenuto del file
# storia = f.read()
# legge i primi 20 caratteri del file
# storia = f.read(20)

# i = 1
# storia = f.read(20)
# while len(storia) > 0:
#  print(i,storia)
#  i = i + 1
# storia = f.read(20)
# print(storia)

line = f.readline()
while line:
    line = line.rstrip('\n')
    print(line, end='')  # fine riga non l'a capo
    g.write(line.upper()+'\n')
    line = f.readline()

f.close()
g.close()


