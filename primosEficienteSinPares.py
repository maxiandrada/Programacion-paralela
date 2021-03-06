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
  cantidad = 1
  maximo = MAX
  for i in range(3,maximo,2):
    if(esPrimo(i)):
      cantidad+=1

  tiempo = time()-startTime
  print ("CPU time secuencial " + str(tiempo))
  return tiempo,cantidad

if __name__ == '__main__':

  comm = MPI.COMM_WORLD
  rank = comm.Get_rank()
  nproc = comm.Get_size()
  maximo = 100000
  cantidad = 1
  cantidadSecuencial = 0
  tiempoParalelo = 0
  tiempoSecuencial = 0
  if rank==0:
    print("Ejecutando Algoritmo Paralelo ")
    startTime=time()
    for i in xrange(1,nproc):
      indiceInferior = i*int(maximo/nproc)
      if(i==maximo):
        indiceSuperior = maximo
      else:
        indiceSuperior = (i+1)*int(maximo/nproc)
      comm.send(indiceInferior, dest=i,tag=1)
      comm.send(indiceSuperior, dest=i, tag=2)
    for i in range(3,1*int(maximo/nproc),2):
      if esPrimo(i):
        cantidad+=1 

    tiempoParalelo=time()-startTime
    print ("CPU time paralelo " + str(tiempoParalelo))
    
    print("Ejecutando Algoritmo Secuencial ")
    tiempoSecuencial,cantidadSecuencial = algoritmoSecuencial(maximo)

  else:
    indiceInferior = comm.recv(source=0,tag=1)
    indiceSuperior = comm.recv(source=0, tag=2)
    
    if(indiceInferior%2==0):
      indiceInferior+=1
    for i in range(indiceInferior,indiceSuperior,2):
      if(esPrimo(i)):
        cantidad +=1 
    #print("rank "+ str(rank)+ " tiene " + str(cantidad))
  data = comm.gather(cantidad, root=0)
  
  if(data!=None):
      cantidad = sum(data)
      print("Paralelo: Cantidad de numeros primos entre 2 y "+str(maximo)+" "+str(cantidad))
      print("Secuencial: Cantidad de numeros primos entre 2 y "+str(maximo)+" "+str(cantidadSecuencial))
      porcentaje =(1-(float(tiempoParalelo)/tiempoSecuencial))*100
      print("El algortimo paralelos es "+str(porcentaje)+"% mas rapido que el secuencial")


