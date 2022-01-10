# 12 to 24


import sys

if len(list(sys.argv))<2:
    print("erreur.")
    sys.exit()

argmument = sys.argv[1]
argument_to_list = list(argmument)
heure=""
minute=""

if len(argument_to_list)==7:
    
    for a in argument_to_list[0:2]:
        heure += a
        if int(heure)>12:
            print("erreur.")
            sys.exit()

    for b in argument_to_list[3:5]:
        minute += b
    
    if argument_to_list[5]=="a":
        print(f"{heure}:{minute}")
    
    elif argument_to_list[5]=="p":
        print(f"{int(heure)+12}:{minute}")
    
    else:
        print("erreur.")
        sys.exit()

elif len(argument_to_list)==6:
    for a in argument_to_list[0:1]:
        heure += a

    for b in argument_to_list[2:4]:
        minute += b
    
    if argument_to_list[4]=="a":
        print(f"{heure}:{minute}")
    
    elif argument_to_list[4]=="p":
        print(f"{int(heure)+12}:{minute}")
    
    else:
        print("erreur.")
        sys.exit()

else:
    print("erreur.")