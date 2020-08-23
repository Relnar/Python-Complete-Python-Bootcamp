import pdb

if __name__ == "__main__":
	x = [1, 3, 4]
	y = 2
	z = 3

	# Set interactive debugging breakpoint
	pdb.set_trace()

	result = x + z
	print(result)
