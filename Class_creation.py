class ConvenientStore:
	''' This program is about Convenient store'''
	def __init__(self,name,price):
		self.name=name
		self.price=price
	def display(self):
		print(self.name,'      ',self.price)

milk=ConvenientStore('Sealtest',5)
egg=ConvenientStore('Omega3',10)
bread=ConvenientStore('wonder',4)
milk.display()
print(egg.__dict__)