def old_macdonald(word):
	firsthalf = word[:3]
	secondhalf = word[3:]
	return firsthalf.capitalize() + secondhalf.capitalize()

def master_yoda(text):
	wordlistreversed = text.split()[: : -1]
	return " ".join(wordlistreversed)

def almost_there(n):
	return abs(100 - n) <= 10 or abs(200 - n) <= 10

def main():
	print("Write a function that capitalizes the first and fourth letters of a name")
	print(old_macdonald("macdonald"))

	print("\nGiven a sentence, return a sentence with the words reversed")
	print(master_yoda("We are ready"))

	print("\nGiven an integer n, return True if n is within 10 of either 100 or 200")
	print("almost_there(90)", almost_there(90))
	print("almost_there(104)", almost_there(104))
	print("almost_there(150)", almost_there(150))
	print("almost_there(209)", almost_there(209))

if __name__ == "__main__":
	main()
