from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA512
import time

# Generar un par de claves ECDSA
def GenerarLlaves():
    llavePrivada = ECC.generate(curve='P-521')
    llavePublica = llavePrivada.public_key()
    return llavePrivada, llavePublica

# Firmar con la clave privada
def Firmar(llavePrivada, mensaje):
    mensaje_hash = SHA512.new(mensaje)
    firma = DSS.new(llavePrivada, 'fips-186-3').sign(mensaje_hash)
    return firma

# Verificar con la clave pública
def Verificar(llavePublica, mensaje, firma):
    mensaje_hash = SHA512.new(mensaje)
    try:
        DSS.new(llavePublica, 'fips-186-3').verify(mensaje_hash, firma)
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