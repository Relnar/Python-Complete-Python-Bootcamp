def spy_game(nums):
	pattern = [0, 0, 7, 'x']
	for num in nums:
		if num == pattern[0]:
			pattern.pop(0)
	return len(pattern) == 1

def count_primes(num):
	primelist = [2]
	for number in range(3, num + 1, 2):
		for prime in primelist:
			if number % prime == 0:
				break
		else:
			primelist.append(number)
	return len(primelist)

def main():
	print("Write a function that takes in a list of integers and returns True if it contains 007 in order")
	print("spy_game([1, 2, 4, 0, 0, 7, 5]) ->", spy_game([1, 2, 4, 0, 0, 7, 5]))
	print("spy_game([1, 0, 2, 4, 0, 5, 7]) ->", spy_game([1, 0, 2, 4, 0, 5, 7]))
	print("spy_game([1, 7, 2, 0, 4, 5, 0]) ->", spy_game([1, 7, 2, 0, 4, 5, 0]))

	print("\nWrite a function that returns the number of prime numbers that exist up to and including a given number")
	print("count_primes(100) ->", count_primes(100))

if __name__ == "__main__":
	main()
