
import math
from collections import Counter

def calculer_redondance(texte):
    """
    Calcule la redondance d'un texte, en supposant un alphabet de 26 lettres.
    """
    n = len(texte)
    if n == 0:
        return 0
    freqs = Counter(texte)
    entropie = -sum((f / n) * math.log2(f / n) for f in freqs.values())
    redondance = 1 - (entropie / math.log2(26))  # log2(26) = entropie max en anglais
    return redondance

# Exemple
texte = "MATHIEU"
print("Redondance:", calculer_redondance(texte))
