#Trié ou pas


import sys

argument = sys.argv[1:]

min = argument[0]
stop = len(argument)
tour = 0
trier = True


for i in argument:
    tour += 1
    if not i.isnumeric():
        print("erreur.")
        sys.exit()
        
    if trier == False:
            print("Pas trié.")
            sys.exit()

    if tour != stop: 
        
        min = i
        if min < argument[tour]:
            trier = True
        else:
            trier = False
    else:
        break

print("Trié")


