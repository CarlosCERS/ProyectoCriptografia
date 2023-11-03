import json
from Algoritmos import chacha20
from Algoritmos import aes_ecb
from Algoritmos import aes_gcm
from Algoritmos import rsa_oaep
from Algoritmos import rsa_pss
from Algoritmos import scrypt
from Algoritmos import sha2_512
from Algoritmos import sha3_512
from Algoritmos import ECDSA_512
from Algoritmos import EdDSA_32
from Herramientas import Graficar

with open("Proyecto/Claves.json","r") as f:
    my_dict=json.load(f)

Key = my_dict["Key"]
Ciclos = int(my_dict["Ciclos"])
Resultado = open('Proyecto/Resultados.txt','w')

################# Cifrado y Descifrado ######################
Vectores = ["Proyecto/Vectores/Texto.txt","Proyecto/Vectores/Requerimiento.pdf","Proyecto/Vectores/Imagen.jpeg"]
for archivo in Vectores:
    titulos=[]
    tiemposEncriptacion=[]
    tiemposDesencriptacion=[]
    print(f"Procesando encriptación y desencriptación de {archivo}")
    
    # Chacha20
    titulos.append('Chacha20')
    Encriptado, Desencriptado = chacha20.calcularTiempo(archivo,Ciclos,Key)
    tiemposEncriptacion.append(Encriptado)
    tiemposDesencriptacion.append(Desencriptado)
    
    # AES_ECB
    titulos.append('AES_ECB')
    Encriptado_AES_ECB, Desencriptado_AES_ECB = aes_ecb.calcularTiempo(archivo,Ciclos,Key)
    tiemposEncriptacion.append(Encriptado_AES_ECB)
    tiemposDesencriptacion.append(Desencriptado_AES_ECB)
    
    # AES_GCM
    titulos.append('AES_GCM')
    Encriptado_AES_GCM, Desencriptado_AES_GCM = aes_gcm.calcularTiempo(archivo,Ciclos,Key)
    tiemposEncriptacion.append(Encriptado_AES_GCM)
    tiemposDesencriptacion.append(Desencriptado_AES_GCM)

    Resultado.write(f'Encriptacion y desencriptacion: {archivo}, {Ciclos} ciclos\n')
    for i in range(len(titulos)):
        Resultado.write(f'{titulos[i]} \n\t Encriptacion:{tiemposEncriptacion[i]} \n\t Desencriptacion:{tiemposDesencriptacion[i]}\n')
    Resultado.write('\n')
    # Graficar.
    Graficar.GraficarEncriptadoDesencriptado(archivo,titulos,tiemposEncriptacion,tiemposDesencriptacion,Ciclos)

############# Encriptación y Desencriptación con RSA_OAEP (Solo se aplica al Texto.txt por el límite de tamaño y se encuentra solo por lo lento que es.)
print(f"Procesando encriptación y desencriptación de Proyecto/Vectores/Texto.txt con RSA_OAEP")
titulos=[]
tiemposEncriptacion=[]
tiemposDesencriptacion=[]

titulos.append('RSA_OAEP')
Encriptado, Desencriptado =  rsa_oaep.calcularTiempo("Proyecto/Vectores/Texto.txt",Ciclos)
tiemposEncriptacion.append(Encriptado)
tiemposDesencriptacion.append(Desencriptado)

Resultado.write(f'Encriptacion y desencriptacion: Proyecto/Vectores/Texto.txt, {Ciclos} ciclos, con RSA_OAEP\n')
for i in range(len(titulos)):
    Resultado.write(f'{titulos[i]} \n\t Encriptacion:{tiemposEncriptacion[i]} \n\t Desencriptacion:{tiemposDesencriptacion[i]}\n')
Resultado.write('\n')
# Graficar.
Graficar.GraficarEncriptadoDesencriptado('texto.txt',titulos,tiemposEncriptacion,tiemposDesencriptacion,Ciclos)

################# Hashing ######################
titulos=['SHA-2','SHA-3']
tiemposHashing=[]
for archivo in Vectores:
    print(f"Procesando Hashing de {archivo}")
    # SHA-2
    # Llamada de la función.
    time_sha2 = sha2_512.hashing2_archivo(archivo, Ciclos)
    tiemposHashing.append(time_sha2)

    # SHA 3
    # Llamada de la función.
    time_sha3 = sha3_512.hashing3_archivo(archivo, Ciclos)
    tiemposHashing.append(time_sha3)

# Escribir resultados en archivo.
Resultado.write(f'Hashing: {Ciclos} ciclos\n')
for i in range(len(titulos)):
    Resultado.write(f'{titulos[i]} \n\t Tiempo:{tiemposHashing[i]} archivo .txt\n')
    Resultado.write(f'\t Tiempo:{tiemposHashing[i+(1*len(titulos))]} archivo .pdf\n')
    Resultado.write(f'\t Tiempo:{tiemposHashing[i+(2*len(titulos))]} archivo .jpeg\n')
Resultado.write('\n')
# Imprimir resultados
Graficar.GraficarComparacionUnSentido(titulos,tiemposHashing, 'Hashing')
    
################# Signing ######################
Vectores = ["Proyecto/Vectores/Texto.txt","Proyecto/Vectores/Requerimiento.pdf","Proyecto/Vectores/Imagen.jpeg"]
for archivo in Vectores:
    titulos=[]
    tiemposFirma=[]
    tiemposVerificacion=[]  
    print(f"Procesando firma y verificación de {archivo}")

    # RSA-PSS
    # Llamada de la función.
    titulos.append('RSA-PSS')
    Firma, Verificacion = rsa_pss.calcularTiempo(archivo, Ciclos)
    tiemposVerificacion.append(Verificacion)
    tiemposFirma.append(Firma)

    # ECDSA P521
    # Llamada de la función.
    titulos.append('ECDSA-P521')
    Firma1, Verificacion1 = ECDSA_512.calcularTiempo(archivo, Ciclos)
    tiemposVerificacion.append(Verificacion1)
    tiemposFirma.append(Firma1)

    # ED25519
    # Llamada de la función.
    titulos.append('ED25519')
    Firma2, Verificacion2 = EdDSA_32.calcularTiempo(archivo, Ciclos)
    tiemposVerificacion.append(Firma2)
    tiemposFirma.append(Verificacion2)

    Resultado.write(f'Firma y verificación: {archivo}, {Ciclos} ciclos\n')
    for i in range(len(titulos)):
        Resultado.write(f'{titulos[i]} \n\t Firma:{tiemposFirma[i]} \n\t Verificacion:{tiemposVerificacion[i]}\n')
    Resultado.write('\n')
    # Graficar.
    Graficar.GraficarFirmaVerificacion(archivo,titulos,tiemposFirma,tiemposVerificacion,Ciclos)


################# Encriptacion contraseña ######################
tiemposContrasena=[]
titulos=[]
print(f"Procesando Hashing para {Key}")

# SHA-2
# Llamada a la función
time_sha2_pass = sha2_512.hashing2_pass(Key, Ciclos)
tiemposContrasena.append(time_sha2_pass)
titulos.append('SHA-2')

# SHA-3
# Llamada a la función
time_sha3_pass = sha3_512.hashing3_pass(Key, Ciclos)
tiemposContrasena.append(time_sha3_pass)
titulos.append('SHA-3')

# Scrypt
# Llamada a la función
titulos.append('Scrypt')
Contraseña = scrypt.Generador(Key, Ciclos)
tiemposContrasena.append(Contraseña)

# Imprimir resultados
Resultado.write(f'Hashing contrasena: {Key}\n')
for i in range(len(titulos)):
    Resultado.write(f'{titulos[i]} \n\t Tiempo:{tiemposContrasena[i]}\n')
Resultado.write('\n')
Graficar.GraficarComparacionContrasena(titulos,tiemposContrasena,Key)

# Finalización.
Resultado.close()
print('Fin del programa.')
