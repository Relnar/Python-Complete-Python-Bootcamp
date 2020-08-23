def main():
	# Tuples are immutable
	t = (1, 2, 3, 2)
	mylist = [1, 2, 3, 2]
	print(t)
	print(mylist)
	# Count number of times 2 is in the tuples
	print(t.count(2))
	# Index of where is the first 2
	print(t.index(2))


if __name__ == "__main__":
	main()

