def main():
	# Open a text file
	myfile = open("myfile.txt")

	# Read a big string
	print(myfile.read())

	# Reset cursor to the file beginning
	myfile.seek(0)

	# readlines => list of lines
	listlines = myfile.readlines()
	print(listlines)

	# Close the file
	myfile.close()

	# The with statement will automatically close new_file
	with open("myfile.txt", mode="r") as new_file:
		for line in new_file.readlines():
			print(line)


if __name__ == "__main__":
	main()

