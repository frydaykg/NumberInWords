from abc import abstractmethod, ABCMeta

class Namer():
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def name(self, num):
		"""Get num in words"""
