import random

def gensquares(n):
	for x in range(n):
		yield x**2

def rand_num(low, high, n):
	for i in range(n):
		yield random.randint(low, high)

if __name__ == "__main__":
	print("Create a generator that generates the squares of numbers of upon some number N.")
	for x in gensquares(10):
		print(x)
	print("")

	print("Create a generator that yields 'n' random numbers between a low and high number (that are inputs).")
	for num in rand_num(1, 10, 12):
		print(num)
	print("")

	my_list = [1, 2, 3, 4, 5]
	# Creates a generator instead of a list comprehension to avoid keeping all the items in memory
	generator_comprehension = (item for item in my_list if item > 3)
	for item in generator_comprehension:
		print(item)
