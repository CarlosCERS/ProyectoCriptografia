from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time

# Genera las llaves
def GenerarLlaves(Primo):
    llavePrivada = RSA.generate(Primo)
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


if __name__ == "__main__":
    file = "Proyecto/Vectores/Texto.txt"
    # Leemos el archivo para convertirlo en "texto plano"
    with open(file,"rb") as file:
        plainText = file.read()

    totalEncriptacion=0
    totalDesencriptacion=0
    for i in range(1,1+1): 
        # Ejemplo de uso
        llavePrivada, llavePublica = GenerarLlaves(3072)
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
