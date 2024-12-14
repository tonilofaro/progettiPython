esempio = [3, 7, 9, 33]
print(esempio)
# stampo un elemento per volta
# print(esempio[0])
# print(esempio[1])
# print(esempio[2])
# print(esempio[3])

# usare il for per stampare gli elementi

for i in range(len(esempio)):
    print(esempio[i])

for v in esempio:
    print(v)

# ciclo su indice e valore
for i, v in enumerate(esempio):
    print(i, v)
