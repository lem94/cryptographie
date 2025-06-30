from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def chiffrer_aes(message, clé):
    """
    Chiffre un message en AES avec padding et IV aléatoire.
    """
    cipher = AES.new(clé, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv, ct_bytes

def dechiffrer_aes(iv, ct, clé):
    """
    Déchiffre un message AES à partir de l'IV et de la clé.
    """
    cipher = AES.new(clé, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode()

# Exemple
clé = get_random_bytes(16)  # 128 bits
iv, chiffré = chiffrer_aes("MATHIEU", clé)
print("Message chiffré (AES) :", chiffré)
print("Message déchiffré :", dechiffrer_aes(iv, chiffré, clé))
