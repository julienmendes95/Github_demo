class Human:

	def __init__(self,name,gender,age,height,weight):
		self.name = name
		self.gender = gender
		self.age = age

	def born(self):
		self.age = 0
		self.life = True

	def grow(self):
		self.age +=1
		if self.age < 21:
			self.height += 0.05  
	
	def gain(self,diffweight):
		self.weight += diffweight

	def loose(self,diffweight):
		self.loose -= diffweight
			
class Man(Human):
	def __init__(self,name,age,height,weight):
		super().__init__(name,'Man',age,height,weight)


		


