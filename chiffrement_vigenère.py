def vigenere_chiffre(texte: str, cle: str) -> str:
    resultat = ""
    cle = cle.lower()
    j = 0
    for char in texte:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decalage = ord(cle[j % len(cle)]) - ord('a')
            resultat += chr((ord(char) - base + decalage) % 26 + base)
            j += 1
        else:
            resultat += char
    return resultat

def vigenere_dechiffre(texte: str, cle: str) -> str:
    resultat = ""
    cle = cle.lower()
    j = 0
    for char in texte:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decalage = ord(cle[j % len(cle)]) - ord('a')
            resultat += chr((ord(char) - base - decalage) % 26 + base)
            j += 1
        else:
            resultat += char
    return resultat

# Exemple d'utilisation
action = input("Voulez-vous chiffrer ou dechiffrer ? (c/d) : ").strip().lower()
texte = input("Entrez le texte : ")
cle = input("Entrez la clé (mot) : ")

if action == 'c':
    print("Texte chiffré :", vigenere_chiffre(texte, cle))
elif action == 'd':
    print("Texte déchiffré :", vigenere_dechiffre(texte, cle))
else:
    print("Action non reconnue.")