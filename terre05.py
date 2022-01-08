import sys

arg1 = sys.argv[1]
arg2 = sys.argv[2]

if arg2 == "0" :
    print("erreur.")
    sys.exit()

if int(arg2) > int(arg1) :
    print("erreur.")
    sys.exit()

else : 
    resultat = int(arg1) // int(arg2)
    reste = int(arg1)%int(arg2)
    print(f"Résultat : {int(resultat)}")
    print(f"Reste : {int(reste)}")