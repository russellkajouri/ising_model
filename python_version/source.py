# #####
#
#
#
# #####
#
from medium import Medium
def main():
	medium = Medium(num = 64, dim = 1, initial_config = "ordered",\
		initial_direction = 1, J = 1, steps = 15000, temp = 2)
	aveE , aveP = medium.Evolution()
	print(aveE, aveP)

main()
