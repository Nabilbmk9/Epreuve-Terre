alphabet = ["a","b","c","d","e","f","g","h",
"i","j","k","l","m","n","o","p","q","r","s",
"t","u","v","w","x","y","z", "\n"]

lettre = input("A partir de qu'elle lettre voulez vous commencer? ")

if lettre in alphabet:
    exo = alphabet[alphabet.index(lettre):]
    for i in exo:
        print(i, end="")

else:
    print("Ce n'est pas une lettre de l'alphabet")