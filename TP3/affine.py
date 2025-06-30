def chiffrement_affine(texte, a, b):
    """
    Chiffrement affine : C = (a * P + b) mod 26
    a et b sont des entiers, avec a premier avec 26.
    """
    def lettre_vers_num(c):
        return ord(c.upper()) - ord('A')

    def num_vers_lettre(n):
        return chr((n % 26) + ord('A'))

    texte = texte.upper().replace(" ", "")
    résultat = ''

    for lettre in texte:
        p = lettre_vers_num(lettre)
        c = (a * p + b) % 26
        résultat += num_vers_lettre(c)

    return résultat

# Exemple
texte = "MATHIEU"
print("Texte chiffré (affine) :", chiffrement_affine(texte, 5, 8))
