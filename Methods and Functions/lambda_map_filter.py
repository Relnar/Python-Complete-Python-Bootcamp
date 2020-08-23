def square(num):
	return num**2

def check_even(num):
	return num%2 == 0

def main():
	print("== map ==")
	array = [1, 2, 3, 4]
	print("square", array, "->", [x for x in map(square, array)])

	print("\n== filter ==")
	print("filter even", array, "->", [x for x in filter(check_even, array)])

	print("\n== lambda expression ==")
	square_lambda = lambda num: num**2
	print("square", array, "->", [x for x in map(square_lambda, array)])
	# Naming the lambda is optional like it's done below
	print("square", array, "->", [x for x in map(lambda num: num**2, array)])
	print("filter even", array, "->", [x for x in filter(lambda num: num%2 == 0, array)])


if __name__ == "__main__":
	main()
