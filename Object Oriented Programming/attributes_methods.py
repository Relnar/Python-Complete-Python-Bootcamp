class Dog():
	# Class object attribute
	# Same for any instance of a class
	species = 'mammal'

	def __init__(self, breed, name, spots):
		self.breed = breed
		self.name = name
		self.spots = spots

	def bark(self):
		print(f"Woof ! My name is {self.name}")


def main():
	dog = Dog('lab', 'Sammy', False)
	print(dog.breed, dog.name, dog.spots, dog.species)
	dog.bark()

	dog2 = Dog('puppy', 'Rex', True)
	# Can use the class name directly for class object attributes
	print(dog2.breed, dog2.name, dog2.spots, Dog.species)

if __name__ == "__main__":
	main()
