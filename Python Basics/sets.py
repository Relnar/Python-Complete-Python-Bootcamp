def main():
	# Sets are unordered and contain unique elements
	myset = set()

	# Add an element
	myset.add(1)
	myset.add(2)
	myset.add(2)		# It will not be added to the set
	print(myset)

	# Casting a list in a set to remove duplicates
	mylist = [1, 2, 3, 2, 1, 2 ,3]
	print(mylist)
	print(set(mylist))

	# Booleans
	boolean = True
	print(boolean)
	print(boolean == False)


if __name__ == "__main__":
	main()

