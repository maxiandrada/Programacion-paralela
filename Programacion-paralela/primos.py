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

def main1():
  startTime=time()
  for i in range(100000):
    print (str(i)+" es primo\n" if esPrimo(i) else str(i)+" no es primo\n")
      
  print ("CPU time " + str(time()-startTime))

def main2():
  comm = MPI.COMM_WORLD
  rank = comm.Get_rank()
  nproc = comm.Get_size()
  if rank==0:
    l=np.arange(10,dtype='i')
    for i in range(1,nproc):
      comm.Send([l[i*int(len(l)/nproc):(i+1)*int(len(l)/nproc)], MPI.INT], dest=i)
    for i in l[:int(len(l)/nproc)]:
      print (str(i)+" es primo\n" if esPrimo(i) else str(i)+" no es primo\n")
  else:
    comm.Recv([l, MPI.INT], source=0)
    for i in l:
      print (str(i)+" es primo\n" if esPrimo(i) else str(i)+" no es primo\n")

if __name__ == '__main__':
  #main1()
  main2()