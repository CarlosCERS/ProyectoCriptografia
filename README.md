# Pimer proyecto de criptografia

Este proyecto está diseñado para poner a prueba distintos algoritmos de criptografía vistos en las clases de Criptografía de la <b>Facultad de Ingeniería</b> de la <b>Universidad Nacional Autónoma de México</b>, los cuales se van a comparar sus tiempos de ejecución con distintos tipos de archivos, desde .txt hasta .jpeg, por lo cual para la verácidad de esto, se usarán los mismos datos de entradas para todos los algoritmos, como las llaves o contraseñas que se usarán, como los ciclos que se repetirán  en estos. Para este proyecto se probrarán los siguientes algoritmos:
<ul>
  <li><b>Chacha20</b> - Llave de 256 bits</li>
  <li><b>AES-EBC</b> - Llave de 256 bits</li>
  <li><b>AES-GCM</b> - Llave de 256 bits</li>
  <li><b>SHA-2</b> - Hash de 512 bits</li>
  <li><b>SHA-3</b> - Hash de 512 bits</li>
  <li><b>Scrypt</b> - Salida de 32 bits</li>
  <li><b>RSA-OAEP</b> - 2048 bits</li>
  <li><b>RSA-PSS</b> - 2048 bits</li>
  <li><b>ECDSA</b> - Curva P-521</li>
  <li><b>EdDSA</b> - Curva 25519</li>
</ul>

Este proyecto tomará los datos que el usuario ingresará <i>cosa que se explicará más adelante</i> y los procesará para todos los algoritmos, repitiendo este proceso de acuerdo al número de ciclos que el propio usuario definió antes; se graficarán los resultados de las pruebas al usuario en distintas etapas, que al cerrarse uno, se ejecutará y mostrará la siguiente parte de la ejecución, dejando al final un resumen a detalle de los resultados de toda la ejecución anotados en un archivo .txt llamado "Resultados.txt".
Debido a que cada algoritmo tiene su propio objetivo y funcionamiento, en este proyecto se ejecutarán en distintos grupos de algorítmos de acuerdo a su función y con los datos asignados.

## Partes de la ejecución
<ul>
  <li>
    <b>Cifrado y Descifrado:</b> En esta etapa se pondrán a comparación la velocidad con la encriptan y desencriptan distintos formtatos de datos, como lo son los archivos .txt, una imágen .jpeg y un documento .pdf, con los algoritmos <i>Chacha20, AES_ECB y AES_GMC</i>.
    <ul>
      <li><b>RSA_OAEP:</b> Este cuarto algoritmo de encriptación y desencriptación, también tendría que estar en este grupo pero, debido al gran tiempo que tarda en hacer sus labores comparados con los otros 3, en la gráfica terminaría opacando al resto, por lo que este se ejecutará separademente del resto.</li>
    </ul>
  </li>
  <li><b>Hashing:</b> En este proceso se probará la velocidad de hashing de los algoritmos de encriptación <i>SHA-2 y SHA.-3</i>, probandolos con los mismos archivos .txt, .pdf y .jpeg</li>
  <li><b>Firmado y verificación:</b> En esta parte, se medirá el tiempo con el que tardan en firmar un archivo .txt, .pdf y .jpeg los algorítmos <i>RSA-PSS, ECDSA-P521 y ED25519</i>.</li>
  <ul>
    <li><b>Hashing de contraseña:</b> En este apartado especial se pondran a prueba la velocidad con la que se aplica hash a una contraseña de los algoritmos <i>SHA-2 y SHA-3</i> en contra del algoritmo  <i>Scrypt</i>.</li>    
  </ul>
</ul>

## Requerimientos
<ul>
  <li>Python 3.9 o superior</li>
  <li>pycryptodome</li>
  <li>matplotlib</li>
  <li>ecdsa</li>
  <li>cryptography</li>
</ul>

## Uso
Para hacer uso del programa, primero se tiene que saber que se divide entre dos carpetas, la de <b>Proyecto</b> y la de <b>Pruebas</b>. Mientras que en la primera carpeta se encuentra el proyecto final que se entrega, en la segunda se encuentran todos los archivos que usamos para experimentos de algoritmos o funciones antes de ingresarlos al proyecto principal.
En la carpeta de <b>Proyecto</b> se encuentran los archivos más importantes:
<ul>
  <li>main.py: Es el archivo dónde se instalan las librerías necesarias para la ejecución del proyecto antes de arrancar el mismo proyecto.</li>
  <li>
    EjecutarProyecto.py: En este archivo se hacen llamadas a todos los algoritmos para su ejecución y análisis.
  </li>
  <li>
    Claves.json: Este es el archivo más importantes para el usuario, ya que dentro de este sencillo archivo podrá modificar alguno valores como la clave que se usarán en distintos algorítmos o el número de ciclos que desee ejecutar en todos los algorítmos, todo esto sin necesidad de modificar directamente el código fuente y que todo esto sea uniforme para todo el proyecto.
  </li>
  <li>
    Texto.txt: Este arhivo si no lo encuentra, se creará al momento de hacer la primera ejecución, y tiene como objetivo el ser una manera alterna de visualizar los resultados más allá de las gráficas porque estas no son del todo claras con valores obtenidos.
  </li>
</ul>

### Si usa Windows
Para ejecutar el proyecto, dentro de la carpeta principal del repositorio (dónde solo se puedan observar las carpetas Proyecto y Pruebas, en terminal ejecute el siguiente código:
</br>
<code>py Proyecto/main.py </code>
</br>
Con todo esto poco a poco van a ir apareciendo las gráficas comparando distintos tiempos de ejecución de distintos algoritmos de encriptación, los cuales tendrá que cerrar para poder avanzar a la siguiente parte del proyecto. Una vez terminado de ejecutar todos los algoritmos y visto todas las gráficas, toda la información recolectada se guardarán en <i>Texto.txt</i> para que usted a detalle pueda analizarlo después.

### Si usa Linux
Debido a que algunas cosas no se podrán hacer de manera automática, se tendrán que hacer de manera manual, por lo que primero se tenrá que instalar las librerias manualmente ejecutando desde dentro de la carpeta principal del repositorio (dónde solo se puedan observar las carpetas Proyecto y Pruebas, en terminal ejecute el siguiente código:
</br>
<code>pip install -r Proyecto/requirements.txt</code>
</br>
Una vez terminado de instalar las liberrias necesarias, desde la misma localización, ejecutar el siguiente código para iniciar el programa:
</br>
<code>python3 Proyecto/EjecutarProyecto.py</code>
