# Using a default argument
def myfunction(name='NoName'):
	"""Hello name

	Args:
		name (string): name

	Returns:
		string: Hello name
	"""
	return "Hello " + name


def main():
	print("== Print doc on the insert function ==")
	help([1, 2].insert)

	print("== Print doc on myfunction ==")
	help(myfunction)

	print("== Function returning a string ==")
	print(myfunction("Sam"))
	print(myfunction())

	print("Ternary if operator (a ? b : c)")
	a = False
	print('Hello' if a else 'Goodbye')


if __name__ == "__main__":
	main()
