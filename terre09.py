#Racine carrée d’un nombre

import sys

tour = 0
chiffre = sys.argv[1]

if not chiffre.isnumeric():
    print("erreur.")
    sys.exit()

for i in range(int(chiffre)):
    tour += 1

    if tour > int(chiffre):
        print("Pas de carré")
    
    else:
        if i*i == int(chiffre):
            print(i)
