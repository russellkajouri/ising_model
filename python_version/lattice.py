# #####
#
#
# #####

from spin import Spin
from random import random
import random
import numpy as np

class Lattice:
	def __init__(self, n, d, mode, dirr, J):
		self.Jfactor = J
		self.number = n
		self.L = []
		self.dim = d
		if self.dim > 2:
			print("Sorry! we do can not afford system with dimension higher than 2 :/")
			exit(0)
			pass

		if mode == "ordered":
			self.ordered_localization(dirr)
		else:
			self.stochastic_localization()
			pass
		#self.display()
		pass
	# --------------------------------------------------------
	def stochastic_localization(self):
		if self.dim == 1:
			for l in range(self.number):
				self.L.append(Spin(random.choice([-1,1]) ))
				pass
			pass

		''' we consider a 1D list, but don't worry, there are many ways to suppose it is a 2D array '''
		if self.dim == 2:
			for I in range(self.number * self.number):
				self.L.append(Spin(random.choice([-1,1]) ))
				pass
			pass
		pass
	# --------------------------------------------------------
	def ordered_localization(self, dirr):
		for l in range(self.number):
			self.L.append(Spin(dirr))
			pass
		for l in range(self.number * self.number):
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
		pass
	''' for 2D, we should be more carefull '''
	def period2D(self, r, c):
		r &= (self.number-1)
		c &= (self.number-1)
		return r * self.number + c
	# --------------------------------------------------------
	def polarization(self):
		polariz = 0.0
		for l in range(self.number):
			polariz += self.L[l].direction
			pass
		return float(polariz / self.number)
	# --------------------------------------------------------
	def energyOf(self, l):
		if self.dim == 1:
			return -1 * self.Jfactor * ( (self.L[l].direction * self.L[self.period(l-1)].direction) + (self.L[l].direction * self.L[self.period(l+1)].direction) )
		elif self.dim == 2:
			r = l // self.number
			c = l - self.number * r
			return -1 * self.Jfactor * self.L[l].direction * ( self.L[self.period2D(r, c+1)].direction +\
					self.L[self.period2D(r, c-1)].direction +\
					self.L[self.period2D(r+1, c)].direction +\
					self.L[self.period2D(r-1,c)].direction )

	# --------------------------------------------------------
	def flipSpin(self, l):
		self.L[l].direction *= -1
	# --------------------------------------------------------
	def chooseSpin(self):
		if self.dim == 1:
			return np.random.randint(0, self.number)
		elif self.dim == 2:
			return np.random.randint(0, self.number*self.number)
	# --------------------------------------------------------
	def MetropoliceStep(self, temp, deltaE):
		if temp == 0:
			return False
		else:
			return True if np.random.random() < np.exp(-deltaE / temp) else False
	# --------------------------------------------------------
	def GetsBackSpin(self, i):
		return self.L[i].direction
	# --------------------------------------------------------
