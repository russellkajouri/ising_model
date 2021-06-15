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
		medium = Medium(num = 512, dim = 1, initial_config = "stochastic",\
			initial_direction = 1, J = 1, steps = 70000, temp = t*dt)
		aveE , aveP = medium.Evolution()
		print("%-5.3f %-5.3f %-5.3f" %(t*dt,aveE, aveP))
		pass
main()
