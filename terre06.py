#Inverser une chaîne

import sys

phrase = list(sys.argv[1])

reverse = phrase[::-1]

for i in reverse:
    print(i, end="")

