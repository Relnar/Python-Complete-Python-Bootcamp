def main():
	print("\nUse for, .split() and if to create a statement that will print out words that start with 's'")
	st = 'Print only the words that start with s in this sentence'
	stwords = [x for x in st.split() if x[0].lower() == 's']
	# Prints the list out on separate lines
	print(*stwords, sep='\n')

	print("\nUse range() to print all the even numbers form 0 to 10")
	print(*list(range(0, 11, 2)), sep='\n')

	print("\nUse list comprehension to create a list of all numbers between 1 and 50 that are divisible by 3")
	divby3 = [x for x in range(1, 51) if x%3 == 0]
	print(divby3)

	print("\nGo through the string below and if the length of a word is even print 'even!'")
	st = "Print every word in this sentence that has an even number of letters"
	print(st)
	for word in st.split():
		if len(word) % 2 == 0:
			print(word, "- even!")

	print("\nWrite a program that prints integers from 1 to 100.")
	print("For multiple of three, print 'Fizz' instead of the number")
	print("For the multiples of five, print 'Buzz.")
	print("For multiples of both three and five, print 'FizzBuzz.")
	for num in range(1, 101):
		if num%3 == 0 and num%5 == 0:
			print(num, "- FizzBuzz")
		elif num%3 == 0:
			print(num, "- Fizz")
		elif num%5 == 0:
			print(num, "- Buzz")
		else:
			print(num, "-", num)

	print("\nUse list comprehension to create a list of the first letters of every word in the string below:")
	st = "Create a list of the first letters of every word in this string"
	print(st)
	firstletter = [x[0] for x in st.split()]
	print(firstletter)


if __name__ == "__main__":
	main()
