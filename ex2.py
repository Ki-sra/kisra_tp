# declaration des list
U1 = []
L = []
U2 = [0, 0, 0]
# processus 
for i in range(3):
    n = int(input("entrez un nombre : "))
    U1.append(n)
for i in range(3):
    while True:
        x = int(input(" entrez une valeur ( just 0 ou 1 ) : "))
        if x == 0 or x == 1:
            L.append(x)
            break
for i in range(3):
    if L[i] == 1:
        U2[i] = U1[i]
    elif L[i] == 0 and i < 2:
        U2[i] = U1[i + 1]
        break
# affichage de resultats
print("U1 :", U1)
print("L :", L)
print("U2 :", U2)
