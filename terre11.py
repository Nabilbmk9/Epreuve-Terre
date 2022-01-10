#24 to 12

import sys

if len(list(sys.argv))<2:
    print("erreur.")
    sys.exit()

argmument = sys.argv[1]
argument_to_list = list(argmument)

pm = "pm"
am = "am"
minute = ""
heure = ""
heure_24_to_12 = ""
deux_points = ":"


if len(argument_to_list) == 5 :

    for a in argument_to_list[3:6]:
        minute += a
    if not minute.isnumeric():
        print("erreur.")
        sys.exit()

    for b in argument_to_list[0:2]:
        heure += b
    
    if not heure.isnumeric():
        print("erreur.")
        sys.exit()
    
    if int(heure) == 12:
        print(heure + ":" + minute + pm)
        sys.exit()

    if int(heure) > 11:
        heure = int(heure) - 12

        heure_24_to_12 = str(heure) + ":" + minute + pm
        print(heure_24_to_12)
    
    else:
        heure_24_to_12 = heure + minute + am
        print(heure_24_to_12)

elif len(argument_to_list) == 4 :
    heure_24_to_12 = argmument + am
    print(heure_24_to_12)

else : 
    print("erreur.")
    
        

        


