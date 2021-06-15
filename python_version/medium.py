# ####
#
#
# #####

from lattice import Lattice

class Medium:
	def __init__(self, num = 64, dim = 1, initial_config = "stochastic",\
			initial_direction = 1, J = 1, steps = 100, temp = 0):

		self.Steps = steps
		self.Temp = temp
		self.latticeSize = num
		self.lattice = Lattice(n = num, d = dim, mode = initial_config, dirr = initial_direction, J = J)
	# --------------------------------------------------------
	def SingleMonteCarloStep(self):
		spin = self.lattice.chooseSpin()
		energy_before_flip = self.lattice.energyOf(spin)
		self.lattice.flipSpin(spin)
		energy_after_flip  = self.lattice.energyOf(spin)

		deltaE = energy_after_flip - energy_before_flip

		if deltaE > 0:
			ans = self.lattice.MetropoliceStep(self.Temp, deltaE)
			if ans == False:
				self.lattice.flipSpin(spin)
	# --------------------------------------------------------
	def MonteCarloSteps(self):
		for l in range(self.latticeSize):
			self.SingleMonteCarloStep()
		return self.lattice.energy(), self.lattice.polarization()
	# --------------------------------------------------------
	def Evolution(self):
		ave_totalE = 0
		ave_orderP = 0
		for s in range(self.Steps):
			totalE, orderP = self.MonteCarloSteps()
			ave_totalE += totalE
			ave_orderP += orderP
			print("%-4.d %-5.3f %-5.3f"%(s, totalE, orderP))
		return (ave_totalE / self.Steps) ,(ave_orderP / self.Steps)
	# --------------------------------------------------------
