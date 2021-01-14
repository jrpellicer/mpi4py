import sys
import numpy
from mpi4py import MPI


if(len(sys.argv) != 2):
    x=1000
else:
    x=eval(sys.argv[1])

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name()

comm.Barrier()
start = MPI.Wtime()

ini = ((x // size) * rank) + 1
if rank == size-1:
    fin=x
else:
    fin = ((x // size) * (rank + 1))

primos = 0
for i in range(ini, fin+1):
    for j in range(2, i):
        if i % j == 0:
            #i es divisor de x, x no es primo
            break #No es necesario buscar mas divisores
    else:
        # OJO, else del bucle For
        # El bucle for ha terminado con normalidad
        # El numero que estabamos comprobando es primo
        primos=primos + 1

print "El Proceso %d de %d en %s ha encontrado %d primos entre el %d y el %d" %(rank,size,name,primos, ini, fin)

comm.Barrier()

if rank==0:
    total = numpy.array(0, dtype='i')
else:
    total = None

sub_total= numpy.array(primos, dtype='i')
comm.Reduce([sub_total, MPI.INT], [total, MPI.INT], op = MPI.SUM, root=0)

comm.Barrier()

if rank==0:
    print "Total de primos encontrados hasta el %d: %d" %(x,total)
    print "Total time: %fs" %(MPI.Wtime()-start)

