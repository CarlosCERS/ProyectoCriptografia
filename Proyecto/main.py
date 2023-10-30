import subprocess
import sys

#Instalación de paquetes en el environment de ejecución.
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Creación de un nuevo entorno virtual de Python.
subprocess.call([sys.executable, "-m", "pip", "install", "virtualenv"])
subprocess.call([sys.executable, "-m", "virtualenv", "Enviroment"])

# Activación del entorno virtual.
if sys.platform == "win32":
    activate_command = "Enviroment\\Scripts\\activate.bat"
else:
    activate_command = "source Enviroment/bin/activate"
subprocess.call(activate_command, shell=True)

# Instalación de las bibliotecas requeridas en el entorno virtual.
install('pycryptodome')
install('matplotlib')
install('ecdsa')
install('cryptography')

# Ejecución del script en el entorno virtual.
subprocess.call(['python','Proyecto/EjecutarProyecto.py'])

# Desactivación del entorno virtual.
subprocess.call('Enviroment\\Scripts\\deactivate.bat', shell=True)