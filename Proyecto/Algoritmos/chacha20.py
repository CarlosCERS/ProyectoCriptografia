from Crypto.Cipher import ChaCha20
import hashlib
import time

# Calcula el tiempo total/promedio que toma chacha20 con n ciclos
def calcularTiempo(file, ciclos, llave):
    # Leemos el archivo para convertirlo en "texto plano"
    with open(file,"rb") as file:
        plainText = file.read()
    #Convertimos la llave en una key de 256 bits.
    secret = hashlib.sha256()
    secret.update(llave.encode('utf-8'))

    totalEncriptacion=0
    totalDesencriptacion=0
    # Ejecutabamos los ciclos.
    for i in range(1,ciclos+1):
        startTime = time.time()
        cipher, ciphertext = Cifrar(plainText, secret)
        finallTime = time.time()
        totalEncriptacion += finallTime - startTime
        startTime = time.time()
        Descifrar(secret,ciphertext,cipher)
        finallTime = time.time()
        totalDesencriptacion += finallTime - startTime
    return totalEncriptacion, totalDesencriptacion
    
# Cifra con chacha20    
def Cifrar(plainText, secret):
    cipher = ChaCha20.new(key=secret.digest())
    ciphertext = cipher.encrypt(plainText)
    return cipher, ciphertext

# Descifra con chacha20
def Descifrar(secret, ciphertext, cipher):
    decipher = ChaCha20.new(key=secret.digest(), nonce=cipher.nonce)
    plaintext = decipher.decrypt(ciphertext)
    return