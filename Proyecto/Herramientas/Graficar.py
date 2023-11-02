import os
import matplotlib.pyplot as plt

# Grafica las comparaciones de encriptado y desencriptado.
def GraficarEncriptadoDesencriptado(archivo, titulos, tiemposCifrado, tiemposDescifrado, ciclos):

    # Colores.
    colors = ['pink', 'yellow', 'blue', 'green', 'red', 'orange']

    # Tamaño o número de gráficas a crear.
    tamanio = len(titulos)

    # Obtener el nombre del archivo.
    file_name = os.path.basename(archivo)

    if(tamanio>1):
        # Declaramos el número de barras a crear.
        fig, ax = plt.subplots(1, tamanio, figsize=(25, 5), sharey=True)

        for i in range(tamanio):
            # Graficar tiempos de encriptación
            ax[i].bar(0, tiemposCifrado[i], color=colors[i])

            # Graficar tiempos de desencriptación
            ax[i].bar(1, tiemposDescifrado[i], color=colors[i])

            ax[i].set_xticks([0, 1])
            ax[i].set_xticklabels(["Cifrado", "Descifrado"])
            ax[i].set_title(f'{titulos[i]}')

        ax[0].set_ylabel("Tiempo promedio (s)")
        # Título
        fig.suptitle(f'Gráficas de tiempo de ejecución de algorítmos de encriptación y desencriptación: {ciclos} ciclos para: {file_name}', fontsize=16)
        plt.show()
    else:
        # Declaramos el número de barras a crear.
        fig, ax = plt.subplots(1, tamanio, figsize=(15, 5), sharey=True)

        # Graficar tiempos de encriptación
        ax.bar(0, tiemposCifrado[0], color=colors[0])

        # Graficar tiempos de desencriptación
        ax.bar(1, tiemposDescifrado[0], color=colors[0])

        ax.set_xticks([0, 1])
        ax.set_xticklabels(["Cifrado", "Descifrado"])
        ax.set_title(f'{titulos[0]}')

        ax.set_ylabel("Tiempo promedio (s)")
        # Título
        fig.suptitle(f'Gráficas de tiempo de ejecución de algorítmos de encriptación y desencriptación: {ciclos} ciclos para: {file_name}', fontsize=16)
        plt.show()


def GraficarFirmaVerificacion(archivo, titulos, tiemposFirma, tiemposVerificado, ciclos):

    # Colores.
    colors = ['purple', 'yellow', 'blue', 'green', 'red', 'orange']

    # Tamaño o número de gráficas a crear.
    tamanio = len(titulos)

    # Obtener el nombre del archivo.
    file_name = os.path.basename(archivo)

    if(tamanio>1):
        # Declaramos el número de barras a crear.
        fig, ax = plt.subplots(1, tamanio, figsize=(25, 5), sharey=True)

        for i in range(tamanio):
            # Graficar tiempos de encriptación
            ax[i].bar(0, tiemposFirma[i], color=colors[i])

            # Graficar tiempos de desencriptación
            ax[i].bar(1, tiemposVerificado[i], color=colors[i])

            ax[i].set_xticks([0, 1])
            ax[i].set_xticklabels(["Firma", "Verificacion"])
            ax[i].set_title(f'{titulos[i]}')

        ax[0].set_ylabel("Tiempo promedio (s)")
        # Título
        fig.suptitle(f'Gráficas de tiempo de ejecución de algorítmos de firma y verificación: {ciclos} ciclos para: {file_name}', fontsize=16)
        plt.show()
    else:
        # Declaramos el número de barras a crear.
        fig, ax = plt.subplots(1, tamanio, figsize=(15, 5), sharey=True)

        # Graficar tiempos de encriptación
        ax.bar(0, tiemposFirma[0], color=colors[0])

        # Graficar tiempos de desencriptación
        ax.bar(1, tiemposVerificado[0], color=colors[0])

        ax.set_xticks([0, 1])
        ax.set_xticklabels(["Firma", "Verificación"])
        ax.set_title(f'{titulos[0]}')

        ax.set_ylabel("Tiempo promedio (s)")
        # Título
        fig.suptitle(f'Gráficas de tiempo de ejecución de algorítmos de firma t verificación: {ciclos} ciclos para: {file_name}', fontsize=16)
        plt.show()



# Grafica las comparaciones de un solo sentido para distintos archivos.
def GraficarComparacionUnSentido(titulos, tiempos, accion):
    # Colores de las barras
    colores = ['green','red','blue']
    
    # Tamaño o número de gráficas a crear.
    tamanio = len(titulos)

    # Crear la figura y los ejes
    fig, ax = plt.subplots(1,tamanio,figsize=(25,5),sharey=True)

    for i in range(tamanio):
        # Graficar tiempos de txt
        ax[i].bar(0, tiempos[i], color=colores[0])

        # Graficar tiempos de txt
        ax[i].bar(1, tiempos[i+(1*tamanio)], color=colores[1])

        # Graficar tiempos de txt
        ax[i].bar(2, tiempos[i+(2*tamanio)], color=colores[2])

        ax[i].set_xticks([0, 1, 2])
        ax[i].set_xticklabels([".txt", ".pdf",".jpeg"])
        ax[i].set_title(f'{titulos[i]}')

    # Etiqueta del eje y
    ax[0].set_ylabel('Tiempo (segundos)')

    # Ajustar el tamaño de la figura
    fig.set_size_inches(25, 5)

    # Título
    fig.suptitle(f'Gráficas de tiempo de ejecución de algorítmos de {accion}', fontsize=16)

    # Mostrar la gráfica
    plt.show()

# Graficar las comparaciones de contraseña.
def GraficarComparacionContrasena(titulos, tiempos, contrasenia):
    # Colores de las barras
    colores = ['blue','red','yellow','green','orange']
    
    # Tamaño o número de gráficas a crear.
    tamanio = len(titulos)

    # Crear la figura y los ejes
    fig, ax = plt.subplots()

    # Graficar las barras
    for i in range(tamanio):
        ax.bar(i*2, tiempos[i], color=colores[i])
        

    espaciados = []
    for i in range(len(titulos)):
        espaciados.append(i*2)

    # Establecer las etiquetas del eje x
    ax.set_xticks(espaciados)
    ax.set_xticklabels(titulos)

    # Ajustar los límites del eje x
    ax.set_xlim([-0.5, espaciados[-1]+1])

    # Etiqueta del eje y
    ax.set_ylabel('Tiempo (segundos)')

    # Ajustar el tamaño de la figura
    fig.set_size_inches(10, 6)

    # Título
    fig.suptitle(f'Tiempo de ejecución para aplicar Hash a la contraseña \'{contrasenia}\'', fontsize=16)

    # Mostrar la gráfica
    plt.show()