class Overload_Demo:
	
	def addNum(self,n1,n2):
		print(n1+n2)
	def addNum(self,n11,n12,n13):
		print(n11+n12+n13)
	
ov=Overload_Demo()
#ov.addNum(1,2,3,4)
ov.addNum(1,2,3)
ov.addNum(1,2)


		
