from random import shuffle
from random import randint

def main():
	print("== range operator ==")
	for num in range(2, 5, 2):
		print(num)

	print("== list casting == ")
	print(list(range(2, 5, 2)))

	# Automatically add an index to each element
	print("== enumerate ==")
	word = 'abcde'
	for index,letter in enumerate(word):
		print(index)
		print(letter)

	# Combines 2 lists in a tuple, it only combines the same number of elements
	print("== zip ==")
	mylist = [1, 2, 3, 4, 5]
	mylist2 = ['a', 'b', 'c']
	for item in zip(mylist, mylist2):
		print(item)

	print("== in test ==")
	print('x' in [1, 2, 3])

	print("== shuffle ==")
	print("mylist: ", mylist)
	shuffle(mylist)
	print("shuffled: ", mylist)

	print("== randint ==")
	print(randint(0, 100))

	print("== input ==")
	result = input("Enter a number: ")
	print("You entered ", result)

	print("== string casting")
	number = "3.12"
	print(number, float(number))


if __name__ == "__main__":
	main()
