import json
from Algoritmos import chacha20
from Herramientas import Graficar

with open("Proyecto/Claves.json","r") as f:
    my_dict=json.load(f)

Key = my_dict["Key"]
Ciclos = int(my_dict["Ciclos"])

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

    # RSA_OAEP
    if(archivo=="Proyecto/Vectores/Texto.txt"):
        titulos.append('RSA_OAEP')
        # Llamada de la función.
        tiemposEncriptacion.append(0)
        tiemposDesencriptacion.append(0)
    
    # Imprimimos los resultados.
    tiemposEncriptacion=[1,2,3,4] #Comentar cuando quieren probar los resultados.
    tiemposDesencriptacion=[5,6,7,8] #Comentar cuando quieren probar los resultados.
    Graficar.GraficarEncriptadoDesencriptado(archivo,titulos,tiemposEncriptacion,tiemposDesencriptacion,Ciclos)

################# Hashing ######################
titulos=['SHA-2','SHA-3','Scrypt']
tiemposHashing=[]
for archivo in Vectores:
    print(f"Procesando Hashing de {archivo}")
    # SHA-2
    # Llamada de la función.
    tiemposHashing.append(0)

    # SHA 3
    # Llamada de la función.
    tiemposHashing.append(0)

    # Scrypt
    # Llamada a la función
    tiemposHashing.append(0)

# Imprimir resultados
tiemposHashing=[1,2,3,4,5,6,7,8,9] #Comentar cuando quieren probar los resultados.
Graficar.GraficarComparacionUnSentido(titulos,tiemposHashing, 'Hashing')
    
################# Signing ######################
titulos=['RSA-PSS','ECDSA P-521', 'EdDSA C25519']
tiemposFirma=[]
for archivo in Vectores:
    print(f"Procesando Signing de {archivo}")

    # RSA-PSS
    # Llamada de la función.
    tiemposFirma.append(0)

    # ECDSA P521
    # Llamada de la función.
    tiemposFirma.append(0)

    # ED25519
    # Llamada de la función.
    tiemposFirma.append(0)

# Imprimir resultados
tiemposFirma=[1,2,3,4,5,6,7,8,9] #Comentar cuando quieren probar los resultados.
Graficar.GraficarComparacionUnSentido(titulos,tiemposFirma, 'Signing')

################# Encriptacion contraseña ######################
tiemposContrasena=[]
titulos=[]
print(f"Procesando Hashing para {Key}")

# SHA-2
# Llamada a la función
tiemposContrasena.append(0)
titulos.append('SHA-2')

# SHA-3
# Llamada a la función
tiemposContrasena.append(0)
titulos.append('SHA-3')

# Scrypt
# Llamada a la función
tiemposContrasena.append(0)
titulos.append('Scrypt')

# Imprimir resultados
tiemposContrasena=[2,4,6] #Comentar cuando quieren probar los resultados.
Graficar.GraficarComparacionContrasena(titulos,tiemposContrasena,Key)

print('Fin del programa.')