class MathDojo(object):
	def __init__(self):
		self.result = 0
	def add(self, *num):
		for a in num:
			if type(a) == list:
				for b in a:
					self.result += b
			elif type(a) == tuple:
				for a in b:
					self.result += b
			else:
				self.result += a
		return self
	def subtract(self, *num):
		for a in num:
			if type(a) == list:
				for b in a:
					self.result -= b
			elif type(a) == tuple:
				for b in a:
					self.result -= b
			else:
				self.result -= a
		return self
	def result(self):
		print self.result
md = MathDojo()
md.add(2).add(2,5).subtract(3,2).result()
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()