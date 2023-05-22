# ####
#
#
# #####

from lattice import Lattice

class Simulator:
	def __init__(self, num = 64, dim = 1, initial_config = "stochastic",\
			initial_direction = 1, J = 1):

		self.Steps = 0
		self.Temp = 0.0
		self.row = num
		self.latticeSize = num if dim == 1 else num * num
		self.dim = dim
		self.lattice = Lattice(n = num, d = dim, mode = initial_config, dirr = initial_direction, J = J)
		self.dumlLag = 0.0
		self.out = None


		self.hasBeenSetTemperature = False
		self.hasDump = False
		pass

	def __del__(self):
		if self.hasDump:
			self.out.close()
		pass

	# --------------------------------------------------------
	def SetTemperature(self, temp):
		self.Temp = temp
		self.hasBeenSetTemperature = True
		pass

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
	def Run(self, Nsteps, lag):
		if not self.hasBeenSetTemperature:
			print("Temperature must be set before starting simulation")
			exit(0)
			pass

		self.Steps = Nsteps
		ave_totalE = 0.0
		ave_orderP = 0.0

		totalE2 = 0.0
		orderP2 = 0.0

		for s in range(self.Steps):
			totalE, orderP = self.MonteCarloSteps()
			ave_totalE += totalE
			ave_orderP += orderP

			totalE2 += totalE * totalE
			orderP2 += orderP * orderP

			if s % lag == 0:
				print(s, "/", Nsteps, sep="", end="\r")

			if self.hasDump and s % self.dumpLag == 0:
				self._WriteTheLattice()
				pass
			pass

		return (ave_totalE / self.Steps) ,(ave_orderP / self.Steps), (totalE2 / self.Steps), (orderP2 / self.Steps)
	# --------------------------------------------------------
	def DumpLattice(self, name, lag, mode = 'w'):
		self.out = open(name, mode = mode)
		self.dumpLag = lag
		self.hasDump = True
		pass

	def _WriteTheLattice(self):
		self.out.write("#{}\n".format(self.latticeSize))
		for i in range(self.latticeSize):

			if self.dim == 1:
				self.out.write("{} {}\n".format(i+0.5, self.lattice.GetsBackSpin(i)))

			elif self.dim == 2:
				r = i // self.row
				c = i - r * self.row
				self.out.write("{} {} {}\n".format(r+0.5, c+0.5, self.lattice.GetsBackSpin(i)))
				pass
			pass
		self.out.write("\n")
		pass
