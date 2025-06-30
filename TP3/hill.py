import numpy as np

def hill_chiffrement(message, matrice_cle):
    """
    Chiffre un message avec le chiffrement de Hill (matrice 2x2).
    Le message doit être en lettres majuscules sans espace.
    """
    def lettre_vers_num(c):
        return ord(c) - ord('A')

    def num_vers_lettre(n):
        return chr((n % 26) + ord('A'))

    # Padding si longueur impaire
    if len(message) % 2 != 0:
        message += 'X'

    # Transformation en vecteurs de 2 lettres
    vecteurs = [np.array([lettre_vers_num(c1), lettre_vers_num(c2)])
                for c1, c2 in zip(message[::2], message[1::2])]

    # Application de la matrice de chiffrement
    chiffré = ''
    for v in vecteurs:
        produit = np.dot(matrice_cle, v) % 26
        chiffré += ''.join(num_vers_lettre(n) for n in produit)

    return chiffré

# Exemple
matrice = np.array([[3, 3], [2, 5]])
texte = "MATHIEU"
print("Texte chiffré (Hill) :", hill_chiffrement(texte, matrice))
