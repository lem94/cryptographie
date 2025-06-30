
from collections import Counter

def indice_coincidence(texte):
    """
    Calcule l'indice de coïncidence d'un texte.
    """
    n = len(texte)
    if n <= 1:
        return 0
    freqs = Counter(texte)
    ic = sum(f * (f - 1) for f in freqs.values()) / (n * (n - 1))
    return ic

# Exemple
texte = "HELLOHELLOOOOOO"
print("Indice de coïncidence:", indice_coincidence(texte))
