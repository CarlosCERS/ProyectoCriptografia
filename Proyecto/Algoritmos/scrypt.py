from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes # Valor de sal aleatorio
import time


def Generador(clave, ciclos):
    for _ in range(ciclos):
        totalTiempo = 0

        # Parámetros de scrypt
        salt = get_random_bytes(16)
        N = 16384
        r = 8
        p = 1
        dklen = 32

        startTime = time.time()
        scrypt(clave, salt=salt, key_len=dklen, N=N, r=r, p=p)
        finallTime = time.time()
        totalTiempo += finallTime - startTime

    return totalTiempo / ciclos
