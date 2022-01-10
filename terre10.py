#Nombre premier

import sys

nombre = sys.argv[1]

if not nombre.isnumeric():
    print("erreur.")
    sys.exit()

elif int(nombre) == 0 :
    print(f"Non, {nombre} n'est pas un nombre premier")

elif int(nombre) == 1 :
    print(f"Non, {nombre} n'est pas un nombre premier")

else:
    for i in range(2, int(nombre)):
        if int(nombre)%i == 0 :
            print(f"Non, {nombre} n'est pas un nombre premier.")
            sys.exit()

    print(f"Oui, {nombre} est un nombre premier")
            
