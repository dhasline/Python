class ObjOne:
	def __init__(self, count):
		self.co=count
	def  __sub__(self,obj):
		return(self.co - obj.co)

one=ObjOne(100)
two=ObjOne(20)
print(one - two)



