def laughter(pattern, text):
	start = 0
	count = 0
	for _ in text:
		start = text.find(pattern, start) + 1
		if (start > 0):
			count += 1
		else:
			return count
	return 0

def paper_doll(text):
	result = ""
	for letter in text:
		# * on a character repeats it
		result += letter * 3
	return result

def blackjack(a, b, c):
	array = [a, b, c]
	arraysum = sum(array)
	if arraysum <= 21:
		return arraysum
	else:
		numof11 = array.count(11)
		if numof11 > 0:
			numof11 = max(1, numof11 - 1)
		arraysum -= 10 * numof11

		if arraysum <= 21:
			return arraysum
		else:
			return "BUST"

def summer_69(arr):
	totalsum = 0
	found6 = False
	for number in arr:
		if number == 6:
			found6 = True
			continue
		if number == 9:
			if found6:
				found6 = False
				continue
		if found6 == False:
			totalsum += number
	return totalsum

def main():
	print("Write a function that counts the number of times a given pattern appears in a string, including overlap")
	print('laughter("hah", "hahahah") ->', laughter("hah", "hahahah"))

	print("\nGiven a string, return a string where for every character in the original there are three characters")
	print("Hello ->", paper_doll("Hello"))
	print("Mississippi ->", paper_doll("Mississippi"))

	print("\nGiven three integers between 1 an 11, if their sum is less than or equal to 21, return their sum.")
	print("If their sum exceeds 21 and there's an eleven, reduc the total sum by 10.")
	print("Finally, if the sum (even after adjustment) exceeds 21, return BUST")
	print("blackjack(5, 6, 7) ->", blackjack(5, 6, 7))
	print("blackjack(9, 9, 9) ->", blackjack(9, 9, 9))
	print("blackjack(9, 9, 11) ->", blackjack(9, 9, 11))
	print("blackjack(9, 11, 11) ->", blackjack(9, 11, 11))
	print("blackjack(11, 11, 11) ->", blackjack(11, 11, 11))

	print("\nReturn the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and")
	print("extending to the next 9 (every 6 will be followed by at least one 9.")
	print("Return 0 for no numbers.")
	print("summer_69([1, 3, 5]) ->", summer_69([1, 3, 5]))
	print("summer_69([4, 5, 6, 7, 8, 9]) ->", summer_69([4, 5, 6, 7, 8, 9]))
	print("summer_69([2, 1, 6, 9, 11]) ->", summer_69([2, 1, 6, 9, 11]))

if __name__ == "__main__":
	main()
