class Human:

	def __init__(self, name, gender, age, height, weight):
		self.name = name
		self.gender = gender
		self.age = age
		self.height = height
		self.weight = weight
		self.life = None

	def born(self):
		self.age = 0
		self.life = True

	def grow(self):
		self.age += 1
		if self.age < 21:
			self.height += 0.05  
	
	def gain(self, diffweight):
		self.weight += diffweight

	def loose(self, diffweight):
		self.loose -= diffweight

	def dead(self):
		self.life = False

			
class Man(Human):
	def __init__(self, name, age, height, weight):
		super().__init__(name, 'Man', age, height, weight)


class Woman(Human):
	def __init__(self, name, age, height, weight):
		super().__init__(name, 'Woman', age, height, weight)


def life_cycle(gender, height0, weight0, age_death):
	name = 'A ' + gender
	h = Human(name, gender, 0, height0, weight0)

	for n in range(age_death+1):
		h.grow()
		
	h.dead()

#life_cycle(gender='Man', height0=0.8, weight0=3, age_death=90)