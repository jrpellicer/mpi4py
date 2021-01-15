# mpi4py
Programas de demo para ejecutar MPI en Python en Ubuntu y Raspbian (clúster de RPi)

## Instalación de mpi4py
Para poder ejecutar los programas de demo en Python es necesario instalar las librerías mpi4py y numpy. 

La primera es la que realmente va a hacer posible la ejecución de los programas en paralelo. El paquete nos instala las librerías de python y también las utilidades necesarias para la ejecución.

    sudo apt-get install -y python-mpi4py python-numpy

## Configuración del ssh
Es necesario que en todos los nodos se instale el ssh-server y se pase la clave pública del usuario que hará la conexión.

    sudo apt-get install -y openssh-server
    ssh-keygen

Copiamos la clave pública del usuario desde el nodo maestro a los esclavos:

    cat ~/.ssh/id_rsa.pub | ssh usuario@X.X.X.X "cat >> .ssh/authorized_keys"

## Copia de los ficheros en el maestro y el resto de los nodos
Clonamos el repositorio en cada uno de los nodos dentro del directorio *mpi4py*

## Creación del machinefile
Creamos en el nodo maestro el fichero *machinefile* que contendrá la lista de los nodos (incluido el maestro) donde se ejecutarán los procesos.

## Ejecución de los programas
Ejecutamos los programas especificando el fichero *machinefile* y la ruta de los programas. Indicamos el número de procesos o si queremos un proceso por nodo.

    mpiexec -np 3  -machinefile machinefile python helloworld.py
    mpiexec -pernode  -machinefile machinefile python helloworld.py
    
    mpiexec -np 8 -machinefile machinefile python primos.py 10000
