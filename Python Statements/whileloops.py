def main():
	x = 0
	while x < 5:
		print(x)
		x += 1
	# Can add an else: statement when the condition ends
	else:
		print("while ended")

	print("pass statement")
	x = [1, 2, 3]
	for _ in x:
		# pass do nothing, it's needed to fix a Python syntax error 
		# As an example, remove the pass statement and it would not compile
		pass

	print("continue statement")
	mystring = "Sammy"
	for letter in mystring:
		if letter == 'a':
			# Goes to the top of the closest enclosing loop
			continue
		print(letter)

	print("break statement")
	mystring = "Sammy"
	for letter in mystring:
		if letter == 'a':
			# Breaks out of the current closest enclosing loop
			break
		print(letter)

	print("End program")


if __name__ == "__main__":
	main()

