# #####
#
#
# #####

from spin import Spin
from random import random
import numpy as np

class Lattice:
	def __init__(self, n, d, mode, dirr, J):
		self.Jfactor = J
		self.number = n
		self.L = []
		if mode == "ordered":
			self.ordered_localization1D(dirr)
		else:
			self.stochastic_localization1D()
			pass
		self.display()
		pass
	# --------------------------------------------------------
	def stochastic_localization1D(self):
		for l in range(self.number):
			self.L.append(Spin(np.random.randint(0,2)*2-1))
			pass
		pass
	# --------------------------------------------------------
	def ordered_localization1D(self, dirr):
		for l in range(self.number):
			self.L.append(Spin(dirr))
			pass
		pass
	# --------------------------------------------------------
	def display(self):
		for l in range(self.number):
			print(self.L[l].direction, end= "")
		print()
		pass
	# --------------------------------------------------------
	def energy(self):
		ene = 0
		for l in range(self.number):
			ene += self.energyOf(l)
		return ene * 0.5 #TODO
	# --------------------------------------------------------
	def period(self, n):
		if n == self.number:
			return n % self.number
		elif n == -1:
			return self.number - 1
		else:
			return n
	# --------------------------------------------------------
	def polarization(self):
		polariz = 0.0
		for l in range(self.number):
			polariz += self.L[l].direction
			pass
		return float(polariz / self.number)
	# --------------------------------------------------------
	def energyOf(self, l):
		return -1 * self.Jfactor * ( (self.L[l].direction * self.L[self.period(l-1)].direction) +\
			(self.L[l].direction * self.L[self.period(l+1)].direction) )
	# --------------------------------------------------------
	def flipSpin(self, l):
		self.L[l].direction *= -1
	# --------------------------------------------------------
	def chooseSpin(self):
		return np.random.randint(0, self.number)
	# --------------------------------------------------------
	def MetropoliceStep(self, temp, deltaE):
		if temp == 0:
			return False
		else:
			return True if np.random.random() > np.exp(-deltaE / temp) else False
