# Trouver la Suisse (lol)

import sys

#Erreur si pas 3 arguments
if len(list(sys.argv)) != 4 :
    print("erreur.")
    sys.exit()

#Erreur si il y a des lettre
for i in list(sys.argv)[1:]:
    if not i.isnumeric():
        print("erreur.")
        sys.exit()

#Erreur si chiffre similaire
aargument = list(sys.argv[1:])

for i in aargument:
    aargument.remove(i)
    if i in aargument:
        print("erreur.")
        sys.exit()

#Code
argument = list(sys.argv)[1:]

permutation = True
j = 0

while permutation:
    permutation = False
    j += 1
    for i in range(0, len(argument)-j):
        print(i)
        if argument[i] > argument[i+1]:
            argument[i], argument[i+1] = argument[i+1], argument[i]
            permutation = True
    
print(argument[1])
