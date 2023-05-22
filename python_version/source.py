# #####
#
#
#
# #####
#
from simulator import Simulator
def main():

	system = Simulator(num = 8, dim = 2, initial_config = "stochastic", initial_direction = 1, J = 1)
	system.DumpLattice(name= "lattice.dat", lag = 100, mode = "w" )

	dT = 0.10
	T = 0.0
	totalT = 2.0
	while T < totalT:
		system.SetTemperature( T )
		aveE , aveP = system.Run( Nsteps = 70000, lag =100 )
		print("%-5.3f %-5.3f %-5.3f" %(T,aveE, aveP))
		T += dT
		pass
	print("#", "-"*70)

main()
