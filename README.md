# Pimer proyecto de criptografia

En este proyecto se pondrán a pruebas distintos algoritmos de criptografía vistos en las clases de Criptografía de la <b>Facultad de Ingeniería</b> de la <b>Universidad Nacional Autónoma de México</b>, además de tenerlos de distintos tamaños de llaves, los cuales son:
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

Este proyecto tomará los datos que el usuario ingresará <i>cosa que se explicará más adelante</i> y los procesará de distintas formas con todos los algoritmos, repitiendo este proceso de acuerdo al número de ciclos que el propio usuario definió antes y despues de ello, se graficarán los resultados mostrándose al usuario quien al cerrar uno, se ejecutará y mostrará el siguiente, dejando al final un resumen a detalle de los resultados de toda la ejecución anotados en un archivo .txt llamado "Resultados.txt".
Debido a que cada algoritmo tiene su propio objetivo y funcionamiento, en este proyecto se ejecutarán en distintos grupos de algorítmos de acuerdo a su función y con los datos asignados.

## Requerimientos
<ul>
  <li>Python 3.11 o superior</li>
</ul>

## Uso
Para hacer uso del programa, primero se tiene que saber que se divide entre dos carpetas, la de <b>Proyecto</b> y la de <b>Pruevas</b>. Mientras que en la primera carpeta se encuentra el proyecto final que se entrega, mientras que en la segunda se encuentran todos los archivos que usamos para experimentos de algoritmos o funciones antes de ingresarlos al proyecto principal.
En la carpeta de <b>Proyecto</b> se encuentran los archivos más importantes:
<ul>
  <li>main.py: Es el archivo dónde se instalan las librerías necesarias para la ejecución del proyecto antes de arrancar el mismo proyecto.</li>
  <li>
    EjecutarProyecto.py: En este archivo se hacen llamadas a todos los algoritmos para su ejecución y análisis.
  </li>
  <li>
    Clajes.json: Este es el archivo más importantes para el usuario, ya que dentro de este sencillo archivo podrá modificar alguno valores como la clave que se usarán en distintos algorítmos o el número de ciclos que desee ejecutar en todos los algorítmos, todo esto sin necesidad de modificar directamente el código fuente y que todo esto sea uniforme para todo el proyecto.
  </li>
  <li>
    Texto.txt: Este arhivo si no lo encuentra, se creará al momento de hacer la primera ejecución, y tiene como objetivo el ser una manera alterna de visualizar los resultados más allá de las gráficas porque estas no son del todo claras con valores obtenidos.
  </li>
</ul>

Para ejecutar el proyecto, dentro de la carpeta principal del repositorio (dónde solo se puedan observar las carpetas Proyecto y Pruebas, en terminal ejecute el siguiente código:
<code>py Proyecto/main.py </code>
Con todo esto poco a poco irán apareciendo gráficas comparando distintos tiempos de ejecución de distintos algoritmos de encriptación, los cuales tendrá que cerrar para poder avanzar a la siguiente parte del proyecto.
