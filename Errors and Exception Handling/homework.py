def ask():
	while True:
		try:
			result = int(input("Please provide number: "))
		except:
			print("Not a number")
		else:
			break

	print(result**2)

def main():
	# Handle the exception thrown by the code below by using try and except blocks
	for i in ['a', 'b', 'c']:
		try:
			print(i**2)
		except TypeError:
			print(f"{i} is not a number")
	print("")

	# Handle the exception thrown by the code below by using try and except blocks.
	# Then use finally block to print "All Done"
	x = 5
	y = 0
	try:
		z = x/y
	except ZeroDivisionError:
		print("Divide-by-zero error")
	finally:
		print("All Done")
	print("")

	# Write a function that asks for an integer and prints the square of it.
	# Use a while loop with a try, except, else block to account for incorrect inputs.
	ask()
	print("")

if __name__ == "__main__":
	main()
