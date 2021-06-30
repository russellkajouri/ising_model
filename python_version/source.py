# #####
#
#
#
# #####
#
from medium import Medium
def main():
	dt = 0.100
	for t in range(1,2):
		print("temp: {:6.4f}".format(t*dt))
		medium = Medium(num = 512, dim = 1, initial_config = "stochastic",\
			initial_direction = 1, J = 1, steps = 70000, temp = t*dt)
		aveE , aveP = medium.Evolution(display=False)
		print("%-5.3f %-5.3f %-5.3f" %(t*dt,aveE, aveP))
		medium.WriteTheLattice()
		print("#", "-"*70)
		pass
main()
