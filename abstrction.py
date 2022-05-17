from abc import *
class Indian(ABC):
	@abstractmethod
	def havingBreakfast(self):
		pass
class Tamil(Indian):
	def havingBreakfast(self):
		print("Idli")
class Kerala(Indian):
	def havingBreakfast(self):
		print("Puttu")
T=Tamil()
K=Kerala()
T.havingBreakfast()
K.havingBreakfast()

