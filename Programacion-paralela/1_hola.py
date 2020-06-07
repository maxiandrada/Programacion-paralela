from mpi4py import MPI
rank = MPI.COMM_WORLD.Get_rank()
size = MPI.COMM_WORLD.Get_size()
name = MPI.Get_processor_name()

print("Hello, world! This is rank %d of %d running on %s" % (rank,size, name))		
