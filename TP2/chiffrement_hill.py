import numpy as np

def nettoyer_texte(texte):
    # Enlève les espaces et met en majuscule
    return ''.join([c for c in texte.upper() if c.isalpha()])

def texte_en_vecteurs(texte, taille_bloc):
    # Découpe le texte en blocs de taille taille_bloc
    blocs = []
    for i in range(0, len(texte), taille_bloc):
        bloc = texte[i:i+taille_bloc]
        if len(bloc) < taille_bloc:
            bloc += 'X' * (taille_bloc - len(bloc))  # Padding avec 'X'
        blocs.append([ord(c) - ord('A') for c in bloc])
    return blocs

def vecteurs_en_texte(vecteurs):
    texte = ''
    for vecteur in vecteurs:
        for val in vecteur:
            texte += chr((val % 26) + ord('A'))
    return texte

def inverse_modulaire_matrice(matrice, mod):
    det = int(round(np.linalg.det(matrice)))
    try:
        det_inv = pow(det % mod, -1, mod)
    except ValueError:
        raise ValueError("La matrice n'est pas inversible modulo 26.")
    matrice_adjoint = np.round(det * np.linalg.inv(matrice)).astype(int) % mod
    return (det_inv * matrice_adjoint) % mod

def chiffrement_hill(texte, cle):
    texte = nettoyer_texte(texte)
    taille_bloc = cle.shape[0]
    blocs = texte_en_vecteurs(texte, taille_bloc)
    chiffres = []
    for bloc in blocs:
        vecteur = np.array(bloc).reshape((taille_bloc, 1))
        chiffre = np.dot(cle, vecteur) % 26
        chiffres.append(chiffre.flatten())
    return vecteurs_en_texte(chiffres)

def dechiffrement_hill(texte, cle):
    texte = nettoyer_texte(texte)
    taille_bloc = cle.shape[0]
    blocs = texte_en_vecteurs(texte, taille_bloc)
    cle_inv = inverse_modulaire_matrice(cle, 26)
    dechiffres = []
    for bloc in blocs:
        vecteur = np.array(bloc).reshape((taille_bloc, 1))
        dechiffre = np.dot(cle_inv, vecteur) % 26
        dechiffres.append(dechiffre.flatten())
    return vecteurs_en_texte(dechiffres)

if __name__ == "__main__":
    print("Chiffrement Hill")
    action = input("Voulez-vous chiffrer ou dechiffrer ? (c/d) : ").strip().lower()
    texte = input("Entrez le texte : ")
    print("Entrez la clé sous forme de matrice carrée (exemple pour 2x2 : 3 3 2 5) :")
    cle_str = input()
    cle_liste = list(map(int, cle_str.strip().split()))
    taille = int(len(cle_liste) ** 0.5)
    cle = np.array(cle_liste).reshape((taille, taille))

    if action == 'c':
        print("Texte chiffré :", chiffrement_hill(texte, cle))
    elif action == 'd':
        try:
            print("Texte déchiffré :", dechiffrement_hill(texte, cle))
        except ValueError as e:
            print("Erreur :", e)
    else:
        print("Action non reconnue.")