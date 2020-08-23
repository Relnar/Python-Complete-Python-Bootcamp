def myfunc(string):
	return "".join([letter.lower() if index%2==0 else letter.upper() for index,letter in enumerate(string)])

def lesser_of_two_evens(a, b):
	if a%2 == 0 and b%2 == 0:
		return min(a, b)
	else:
		return max(a, b)

def animal_crackers(animal):
	words = animal.split()
	if len(words) != 2:
		return False
	return words[0][0].lower() == words[1][0].lower()

def other_side_of_seven(num):
	# (7 - num) * 2 + 7
	return 21 - 2*num


def main():
	print("Anthropomorphism ->", myfunc("Anthropomorphism"))

	print("\nWrite a function that returns the lesser of two given numbers if both numbers are even,")
	print("returns the greater if one or both numbers are odd")
	print("lesser_of_two_evens(2, 4) ->", lesser_of_two_evens(2, 4))
	print("lesser_of_two_evens(2, 5) ->", lesser_of_two_evens(2, 5))
	print("lesser_of_two_evens(7, 3) ->", lesser_of_two_evens(7, 3))
	print("lesser_of_two_evens(9, 2) ->", lesser_of_two_evens(9, 2))

	print("\nWrite a function that takes two-word string and returns True if both words begin with the same letter")
	print("Levelheaded Llama", animal_crackers("Levelheaded Llama"))
	print("Crazy Kangoroo", animal_crackers("Crazy Kangoroo"))

	print("\nGiven a value, return a value that is twice as far away on the other side of 7")
	print("4 ->", other_side_of_seven(4))
	print("12 ->", other_side_of_seven(12))


if __name__ == "__main__":
	main()
