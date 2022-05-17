class House:
	def __init__(self,name,sex,age,role):
		self.name=name
		self.sex=sex
		self.age=age
		self.role=role
	def display(self):
		return ('Name : {} Sex: {} Age:  {} Role: {} '.format(self.name,self.sex,self.age,self.role )
	
member1= House("Dhasline", "Female", 43, "House wife")
h2 = House('Joseley','Male','45','Physical Therpist')
print(member1.display())
print(h2.display())
