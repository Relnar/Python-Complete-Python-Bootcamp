def addValue(x, y):
	value = 0
	try:
		value = x + y
	except:
		print(f"Error adding {x} and {y}")
	else:
		print(f"Adding {x} and {y} was successful")
	finally:
		return value

	# This return statement will be skip because of the finally
	return -1

def writeFile(mode):
	try:
		print(f"Trying to write to a file with mode {mode}")
		f = open("testfile.txt", mode)
		f.write("Test line")
	except TypeError:
		print("Type error")
	except OSError:
		print("OS error")
	finally:
		f.close()
		print("finally is always ran")

def askForInt():
	while True:
		try:
			result = int(input("Please provide number: "))
		except:
			print("Not a number")
		else:
			break

	return result

def main():
	value = addValue(5, 6)
	print(value)
	value = addValue(5, "6")
	print(value)
	print("")

	writeFile("w")
	print("")

	# Trying to write to a read-only file to generate OSError
	writeFile("r")
	print("")

	askForInt()

if __name__ == "__main__":
	main()
