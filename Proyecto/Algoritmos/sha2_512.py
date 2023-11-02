import hashlib, time

tamanio = 10240 #10KB, uso como estándar

def apertura_archivo(archivo):
    sha2_512 = hashlib.sha512()
    #abrimos el archivo como lectura en binario para sencillez del hash
    with open(archivo, 'rb') as f:
        #a continuacion hacemos la división en bloques para no llenar la memoria con archivos grandes
        while True:
            bloques = f.read(tamanio)
            if not bloques:
                break
            #vamos actualizando el objeto bloque a bloque
            sha2_512.update(bloques)
    #Pasamos el hash a hexadecimal
    return sha2_512.hexdigest()

def hash2_archivo(archivo):
    #medimos el tiempo que tarda en aplicar el hash
    inicio = time.time()
    apertura_archivo(archivo)
    fin = time.time()
    return fin - inicio

def hash2_pass(contrasena):
    #medimos el tiempo que tarda en aplicar el hash
    inicio = time.time()
    #en esta funcion unicamente aplicamos hash al pass
    sha2_512 = hashlib.sha512()
    sha2_512.update(contrasena.encode('UTF-8'))
    sha2_512 = sha2_512.hexdigest()
    fin = time.time()
    return fin - inicio

def hashing2_archivo(archivo, ciclos):
    """Obtiene el tiempo promedio de ejecución de cada algoritmo de hash usando una muestra de 1000 iteraciones"""
    time_sha2_512 = 0
    #Realizamos las iteraciones de las muestra representativa
    for _ in range(ciclos):
        time_sha2_512 += hash2_archivo(archivo)
 
    return time_sha2_512 / ciclos

def hashing2_pass(password, ciclos):

    time_sha2_512 = 0
    #Realizamos las iteraciones de las muestra representativa
    for _ in range(ciclos):
        time_sha2_512 += hash2_pass(password)
        
    return time_sha2_512 / ciclos