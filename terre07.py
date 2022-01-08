import sys

argument = [sys.argv]
phrase = sys.argv[1]
phrase_to_list = list(phrase)
total =0

if len(argument)!= 1 or phrase.isnumeric():
    print("erreur.")
    sys.exit()

else:
    for i in phrase_to_list : 
        total+=1

print(total)

