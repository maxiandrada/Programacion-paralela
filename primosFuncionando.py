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





def algoritmoSecuencial(MAX):
  startTime=time()
  cantidad = 0
  maximo = MAX
  for i in range(maximo):
    if(esPrimo(i)):
      cantidad+=1

    
  print ("CPU time secuencial " + str(time()-startTime))
  return cantidad


if __name__ == '__main__':

  comm = MPI.COMM_WORLD
  rank = comm.Get_rank()
  nproc = comm.Get_size()
  maximo = 1000000
  cantidad = 0
  cantidadSecuencial = 0
  if rank==0:
    print("Ejecutando Algoritmo Paralelo ")
    startTime=time()
    l=np.arange(maximo,dtype='i')
    for i in range(1,nproc):
      comm.Send([l[i*int(len(l)/nproc):(i+1)*int(len(l)/nproc)], MPI.INT], dest=i)
    for i in l[:int(len(l)/nproc)]:
      if esPrimo(i):
        cantidad+=1 
    
    print ("CPU time paralelo " + str(time()-startTime))
    
    print("Ejecutando Algoritmo Secuencial ")
    cantidadSecuencial = algoritmoSecuencial(maximo)

  else:
    l = np.zeros(maximo,dtype='i')
    comm.Recv([l,maximo, MPI.INT],source=0)
    for i in l:
      if(esPrimo(i)):
        cantidad +=1 
    #print("rank "+ str(rank)+ " tiene " + str(cantidad))
  data = comm.gather(cantidad, root=0)
  
  if(data!=None):
      cantidad = sum(data)
      print("Cantidad de numeros primos entre 2 y "+str(maximo)+" "+str(cantidad))
      print("Cantidad de numeros primos entre 2 y "+str(maximo)+" "+str(cantidadSecuencial))
      print("El algortimo paralelos es "+str(float(cantidad/cantidadSecuencial)*100)+"% mas rapido que el secuencial")







  

