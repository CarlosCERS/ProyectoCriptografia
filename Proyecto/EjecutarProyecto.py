import json
from Algoritmos import chacha20
from Algoritmos import rsa_oaep
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
    # Llamada de la función.
    tiemposEncriptacion.append(0)
    tiemposDesencriptacion.append(0)
    
    # AES_CBC
    titulos.append('AES_CBC')
    # Llamada de la función.
    tiemposEncriptacion.append(0)
    tiemposDesencriptacion.append(0)

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
Graficar.GraficarEncriptadoDesencriptado(archivo,titulos,tiemposEncriptacion,tiemposDesencriptacion,Ciclos)

################# Hashing ######################
titulos=['SHA-2','SHA-3','Scrypt']
tiemposHashing=[]
for archivo in Vectores:
    print(f"Procesando Hashing de {archivo}")
    # SHA-2
    # Llamada de la función.
    tiemposHashing.append(1)

    # SHA 3
    # Llamada de la función.
    tiemposHashing.append(2)

    # Scrypt
    # Llamada a la función
    tiemposHashing.append(3)

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
titulos=['RSA-PSS','ECDSA P-521', 'EdDSA C25519']
tiemposFirma=[]
for archivo in Vectores:
    print(f"Procesando Signing de {archivo}")

    # RSA-PSS
    # Llamada de la función.
    tiemposFirma.append(4)

    # ECDSA P521
    # Llamada de la función.
    tiemposFirma.append(5)

    # ED25519
    # Llamada de la función.
    tiemposFirma.append(6)


Resultado.write(f'Signing: {Ciclos} ciclos\n')
for i in range(len(titulos)):
    Resultado.write(f'{titulos[i]} \n\t Tiempo:{tiemposFirma[i]} archivo .txt\n')
    Resultado.write(f'\t Tiempo:{tiemposFirma[i+(1*len(titulos))]} archivo .pdf\n')
    Resultado.write(f'\t Tiempo:{tiemposFirma[i+(2*len(titulos))]} archivo .jpeg\n')
Resultado.write('\n')
# Imprimir resultados
Graficar.GraficarComparacionUnSentido(titulos,tiemposFirma, 'Signing')

################# Encriptacion contraseña ######################
tiemposContrasena=[]
titulos=[]
print(f"Procesando Hashing para {Key}")

# SHA-2
# Llamada a la función
tiemposContrasena.append(1)
titulos.append('SHA-2')

# SHA-3
# Llamada a la función
tiemposContrasena.append(2)
titulos.append('SHA-3')

# Scrypt
# Llamada a la función
tiemposContrasena.append(3)
titulos.append('Scrypt')

# Imprimir resultados
Resultado.write(f'Hashing contrasena: {Key}\n')
for i in range(len(titulos)):
    Resultado.write(f'{titulos[i]} \n\t Tiempo:{tiemposContrasena[i]}\n')
Resultado.write('\n')
Graficar.GraficarComparacionContrasena(titulos,tiemposContrasena,Key)

# Finalización.
Resultado.close()
print('Fin del programa.')