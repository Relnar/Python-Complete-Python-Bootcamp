# Base class
class Animal():
	def __init__(self):
		print("Animal created")

	def who_am_i(self):
		print("I am an animal")

	def eat(self):
		print("I am eating")

	# Pure virtual function
	def speak(self):
		raise NotImplementedError("Subclass must implement this abstract method")

# Dog derives from Animal
class Dog(Animal):
	# Class object attribute
	# Same for any instance of a class
	species = 'mammal'

	def __init__(self, breed, name, spots):
		# Initialize the base class
		Animal.__init__(self)

		self.breed = breed
		self.name = name
		self.spots = spots

	def bark(self):
		print(f"Woof ! My name is {self.name}")

	# Override method
	def who_am_i(self):
		# Can call the base class if necessary
		Animal.who_am_i(self)
		print("I am a dog")


def main():
	myanimal = Animal()
	myanimal.who_am_i()
	myanimal.eat()
	print("")

	dog = Dog('lab', 'Sammy', False)
	print(dog.breed, dog.name, dog.spots, dog.species)
	dog.bark()
	dog.who_am_i()
	dog.eat()

if __name__ == "__main__":
	main()
