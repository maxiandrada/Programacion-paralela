from mpi4py import MPI
from time import time

Tini = time()
rank = MPI.COMM_WORLD.Get_rank()
size = MPI.COMM_WORLD.Get_size()
name = MPI.Get_processor_name()
TFin = time()-Tini
print("Hello, world! This is rank %d of %d running on %s: Time(%f min)" % (rank,size, name, TFin/60))		
