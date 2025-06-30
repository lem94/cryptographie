from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generer_cles_rsa():
    """
    Génère une paire de clés RSA.
    """
    clé = RSA.generate(2048)
    return clé, clé.publickey()

def chiffrer_rsa(message, clé_publique):
    """
    Chiffre un message avec une clé publique RSA.
    """
    cipher = PKCS1_OAEP.new(clé_publique)
    return cipher.encrypt(message.encode())

def dechiffrer_rsa(chiffré, clé_privée):
    """
    Déchiffre un message avec une clé privée RSA.
    """
    cipher = PKCS1_OAEP.new(clé_privée)
    return cipher.decrypt(chiffré).decode()

# Exemple
privée, publique = generer_cles_rsa()
chiffré = chiffrer_rsa("MATHIEU", publique)
print("Message chiffré (RSA) :", chiffré)
print("Message déchiffré :", dechiffrer_rsa(chiffré, privée))
