class OurClass(object):
	"""Class docstring."""
	
	def __init__(self, input_arg1, input_arg2):
		"""Method docstring."""
		self.arg1 = input_arg1
		self.arg2 = input_arg2
	
	def printargs(self):
		"""Method docstring."""
		print self.arg1
		print self.arg2
		
instance = OurClass('first argument', 'second arguement')
print type(instance)
instance.printargs()
print instance.arg1
print dir(instance)