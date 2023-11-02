from Crypto.Cipher import AES
import hashlib
import time

# Calcula el tiempo total/promedio que toma AES con n ciclos
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
    
# Cifra con AES GCM   
def Cifrar(plainText, secret):
    private_key=secret.digest()
    cipher = AES.new(private_key, AES.MODE_GCM)
    ciphertext = cipher.encrypt(plainText)
    return cipher, ciphertext

# Descifra con AES GCM
def Descifrar(secret, ciphertext, cipher):
    private_key=secret.digest()
    decipher = AES.new(private_key, AES.MODE_GCM)
    plaintext = decipher.decrypt(ciphertext)
    return

