
import math
from collections import Counter

def calculer_entropie(texte):
    """
    Calcule l'entropie d'un texte selon la formule de Shannon.
    """
    n = len(texte)
    freqs = Counter(texte)
    entropie = -sum((f / n) * math.log2(f / n) for f in freqs.values())
    return entropie

# Exemple d'utilisation
texte = "MATHIEU"
print("Entropie:", calculer_entropie(texte))
