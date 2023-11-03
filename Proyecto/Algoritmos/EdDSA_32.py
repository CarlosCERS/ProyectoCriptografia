from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization, hashes
import time

# Generar un par de claves EdDSA con la curva curve25519 (Ed25519)
def GenerarLlaves():
    llavePrivada = ed25519.Ed25519PrivateKey.generate()
    llavePublica = llavePrivada.public_key()
    return llavePrivada, llavePublica

# Firmar con la clave privada
def Firmar(llavePrivada, mensaje):
    firma = llavePrivada.sign(mensaje)
    return firma

# Verificar con la clave pública
def Verificar(llavePublica, mensaje, firma):
    try:
        llavePublica.verify(firma, mensaje)
        return True
    except Exception as e:
        print(f"Error al verificar la firma: {e}")
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

