# DECLARER LES 3 TABLEAU
t1 = [1,4,6,10,20,34]
t2 = [2,5,8,14,25,39]
t3 = []
# calcule de  la somme des éléments des deux tableaux de départ
for i in range(len(t1)):
    t3.append(t1[i] + t2[i])
# affichage  de 3 eme tableau
print("Tableau 3:", t3)
