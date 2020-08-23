class Sample():
	def __init__(self, test=0):
		self.test = test

def main():
	# Default constructor
	sample = Sample()
	print(sample.test)

	# Constructor with an argument
	sample2 = Sample(2)
	print(sample2.test)

	# Attributes are public
	sample2.test = 3
	print(sample2.test)

	# Naming the argument
	sample4 = Sample(test=4)
	print(sample4.test)

if __name__ == "__main__":
	main()
