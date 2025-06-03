def cesar_chiffre(mot: str, cle: int) -> str:
    resultat = ""
    for char in mot:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            resultat += chr((ord(char) - base + cle) % 26 + base)
        else:
            resultat += char
    return resultat

def cesar_dechiffre(mot: str, cle: int) -> str:
    return cesar_chiffre(mot, -cle)

# Exemple d'utilisation
action = input("Voulez-vous chiffrer ou dechiffrer ? (c/d) : ").strip().lower()
mot = input("Entrez le mot : ")
cle = int(input("Entrez la clé (nombre entier) : "))

if action == 'c':
    print("Mot chiffré :", cesar_chiffre(mot, cle))
elif action == 'd':
    print("Mot déchiffré :", cesar_dechiffre(mot, cle))
else:
    print("Action non reconnue.")