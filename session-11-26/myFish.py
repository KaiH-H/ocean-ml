class Fish:
	def __init__(self, name='fish',hunger=0,happiness = 10):
		self.name = name
		self.hunger = hunger
		self.happiness = happiness
		# add 4 other data fields 

	def eat(self):
		# what happens hunger and happiness when the fish eats? --> hunger decreases, happiness increases
		self.hunger=self.hunger-1
		self.happiness = self.happiness+1
		print(self.name + " has eaten.")

	def swim(self):
		# what happens to hunger and happiness when the fist swims? --> Both increase
		self.hunger = self.hunger+1
		self.happiness = self.happiness+1
		print(self.name + " has swum.")

	#what other things does the fish do besides eat and swim?'
	def beg(self):
		self.hunger = self.hunger+1
		self.happiness = self.happiness-1
		print(self.name + " has begged, but you did not give in.")

fish = Fish("Glub")
fish.eat()

