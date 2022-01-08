import sys


if len(sys.argv) != 3 :
    print("erreur.")
    sys.exit()


chiffre1 = sys.argv[1]
chiffre2 = sys.argv[2]
total = 1


if chiffre1.isnumeric() and chiffre2.isnumeric():
    if int(chiffre2) < 0 :
        print("erreur.")
        sys.exit()
    
    elif chiffre2 == 0:
        print("1")
        sys.exit()

    else :
        for i in range(1, int(chiffre2)+1):
            total = total * int(chiffre1)

        print(total)

else :
    print("erreur.")

