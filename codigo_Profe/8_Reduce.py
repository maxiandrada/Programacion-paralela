import numpy
from mpi4py import MPI
comm = MPI.COMM_WORLD
 
rank = comm.Get_rank()
rankF = numpy.array(float(rank))
print (rankF)
total = numpy.zeros(1)
print (total)

comm.Reduce(rankF,total, op=MPI.MAX)
print (total)
