from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time

# Genera las llaves
def GenerarLlaves():
    llavePrivada = RSA.generate(2048)
    llavePublica = llavePrivada.publickey()
    return llavePrivada,llavePublica

# Cifra con la llave pública.
def Cifrar(llavePublica, plaintext):
    cipher = PKCS1_OAEP.new(llavePublica)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

# Descifra con la llave pública.
def Descifrar(llavePrivada, ciphertext):
    decipher = PKCS1_OAEP.new(llavePrivada)
    plaintext = decipher.decrypt(ciphertext)    
    return plaintext


def calcularTiempo(file, ciclos):
    # Leemos el archivo para convertirlo en "texto plano"
    with open(file,"rb") as file:
        plainText = file.read()

    totalEncriptacion=0
    totalDesencriptacion=0
    llavePrivada, llavePublica = GenerarLlaves()
    for i in range(1,ciclos+1):
        # Cifrado
        startTime = time.time()
        ciphertext = Cifrar(llavePublica, plainText)
        finallTime = time.time()
        totalEncriptacion += finallTime - startTime
        # Descifrado
        startTime = time.time()
        plaintext = Descifrar(llavePrivada, ciphertext)
        finallTime = time.time()
        totalDesencriptacion += finallTime - startTime
    return totalEncriptacion, totalDesencriptacion
