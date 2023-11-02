from Crypto.PublicKey import RSA
from Crypto.Signature import pss
from Crypto.Hash import SHA256
import time

# Generar un par de claves RSA
def GenerarLlaves():
    llavePrivada = RSA.generate(2048)
    llavePublica = llavePrivada.publickey()
    return llavePrivada, llavePublica

# Firmar con la clave privada
def Firmar(llavePrivada, mensaje):
    mensaje_hash = SHA256.new(mensaje)
    firma = pss.new(llavePrivada).sign(mensaje_hash)
    return firma

# Verificar con la clave pública
def Verificar(llavePublica, mensaje, firma):
    mensaje_hash = SHA256.new(mensaje)
    try:
        pss.new(llavePublica).verify(mensaje_hash, firma)
        return True
    except (ValueError, TypeError):
        return False

def calcularTiempo(file, ciclos):
    # Leemos el archivo 
    with open(file,"rb") as file:
        mensaje = file.read()

    totalFirmado = 0
    totalVerificado = 0
    llavePrivada, llavePublica = GenerarLlaves()
    for i in range(1, ciclos + 1):
        # Firmar
        startTime = time.time()
        firma = Firmar(llavePrivada, mensaje)
        finallTime = time.time()
        totalFirmado += finallTime - startTime

        # Verificar
        startTime = time.time()
        verificado = Verificar(llavePublica, mensaje, firma)
        finallTime = time.time()
        totalVerificado += finallTime - startTime

    return totalFirmado, totalVerificado

