# Generator function
def create_cubes(n):
	for x in range(n):
		# yield to use as a generaor
		yield x**3

def fibonacci(n):
	a = 1
	b = 1
	for _ in range(n):
		yield a
		a, b = b, a+b

if __name__ == "__main__":
	for x in create_cubes(10):
		print(x)
	print("")

	for x in fibonacci(10):
		print(x)
	print("")

	# Store the generator to generate one at a time
	g = fibonacci(5)
	for _ in range(5):
		# next value
		print(next(g))
	print("")

	# Create an iterator on a string to enumerate the letters
	s = "Hello"
	s_iter = iter(s)
	for _ in range(len(s)):
		print(next(s_iter))