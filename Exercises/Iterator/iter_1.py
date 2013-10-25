class MyIterator(object):
	def __init__(self, step):
		self.step = step
	def next(self):
		print "Self.step",self.step
		"""Returns the next element."""
		if self.step == 0:
			raise StopIteration
		self.step -= 1
		return self.step
	def __iter__(self):
		"""Returns the iterator itself."""
		print "Self", self
		return self

print MyIterator(4).next()
#for el in MyIterator(4):
#	print el
