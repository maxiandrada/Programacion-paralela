from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

data = (rank+1)**2
print "before gather, data on rank %d is: "%rank, data
data = comm.gather(data, root=0)
print "data on rank: %d is: "%rank, data