chiffre = input("choisissez un chiffre : ")

if chiffre.isnumeric():
    if int(chiffre)%2 == 0 : 
        print("pair")

    elif int(chiffre)%2 == 1 :
        print("impaire")

else : 
    print("Tu ne me la mettra pas a l'envers")