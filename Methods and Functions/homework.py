import math
import collections
import string

def vol(rad):
	return 4.0 / 3.0 * math.pi * rad**3

def ran_check(num, low, high):
	return num in range(low, high + 1)

def up_low(str):
	letters = list(str)
	lowercount = 0
	uppercount = 0
	for letter in letters:
		if letter.islower():
			lowercount += 1
		elif letter.isupper():
			uppercount += 1
	print("Nb upper case letters:", uppercount)
	print("Nb lower case letters:", lowercount)

def unique_list(l):
	a = []
	for x in l:
		if x not in a:
			a.append(x)
	return a

def multiply(numbers):
	product = 1
	for num in numbers:
		product *= num
	return product

def palindrome(s):
	return s[::-1] == s

def pangram(str1, alphabet=string.ascii_lowercase):
	trimedstr = str1.replace(" ", "")
	trimedstr = trimedstr.lower()
	setstr = set(trimedstr)
	return len(setstr) == len(alphabet)

def main():
	print("Write a function that computes the volume of a sphere given its radius")
	print("rad = 3 ->", vol(3))

	print("\nWrite a function that checks whether a number is in a given range (Inclusive of high and low).")
	print("ran_check(3, 4, 6) ->", ran_check(3, 4, 6))
	print("ran_check(3, 3, 6) ->", ran_check(3, 3, 6))
	print("ran_check(6, 4, 6) ->", ran_check(6, 4, 6))

	print("\nWrite a function that accepts a string and calculate the number of upper case")
	print("letters and lower case letters.")
	st = "Hello Mr. Rogers, how are you this fine Tuesday?"
	print(st)
	up_low(st)

	print("\nWrite a function that takes a list and returns a new list with unique elements of the first list.")
	print("[1,1,1,1,2,2,3,4,4,4,4,5,5,5,5] ->", unique_list([1,1,1,1,2,2,3,4,4,4,4,5,5,5,5]))

	print("\nWrite a function to multiply all the numbers in a list.")
	print("[1, 2, 3, -4] ->", multiply([1, 2, 3, -4]))

	print("\nWrite a function that checks whether a passed string is a palindrome or not.")
	print("helleh", palindrome("helleh"))
	print("hello", palindrome("hello"))

	print("\nWrite a function to check whether a string is pangram or not.")
	print("The quick brown fox jumps over the lazy dog", pangram("The quick brown fox jumps over the lazy dog"))
	print("The quick brown fox jumps over the dog", pangram("The quick brown fox jumps over the dog"))

if __name__ == "__main__":
	main()
