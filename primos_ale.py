import math
from time import time
from mpi4py import MPI
import numpy as np


def esPrimo(n):
  if n % 2 == 0:
    return False

  sqrt_n = int(math.floor(math.sqrt(n)))
    
  for i in range(3, sqrt_n + 1, 2):
    if n % i == 0:
      return False
    
  return True


def main1(parametro):
  startTime=time()
  cant=0
  for i in range(parametro):
    if esPrimo(i):
      cant += 1
  print ("Tiempo CPU secuencial: " + str(time()-startTime)+". Cantidad de primos: "+str(cant))

def main2(parametro):
  startTime = time()
  comm = MPI.COMM_WORLD
  rank = comm.Get_rank()
  nproc = comm.Get_size()
  
  cant = 0
  
  ini = rank*int(parametro/nproc)
  fin = (rank + 1)*int(parametro/nproc)
  for i in range(ini,fin):
    if esPrimo(i):
      cant += 1
  lista = comm.gather(cant, root=0)
  if rank==0:
    print ("Tiempo CPU paralelo: "+str(time()-startTime)+".Cantidad de primos: "+str(sum(lista)))
    main1(parametro)
        
if __name__ == '__main__':
  parametro = 10000000
  main2(parametro)