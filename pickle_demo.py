import pickle
class Student:
	def __init__(self,name,id):
		self.name=name
		self.id=id
	def display(self):
		print(self.name)
		print(self.id)
#dumping or writing
stu=Student('Dhasline',123)
stu1=Student('Rini',124)
f=open("sample.jpg","wb")
pickle.dump(stu,f)
print('dumped successfully')

#undumping or unload or unpickling or reading from file

#f=open('sample.jpg','rb')
#stu=pickle.load(f)
#stu.display()