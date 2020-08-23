from collections import Counter

if __name__ == "__main__":
	# Counts number of occurences in a list store in a dictionary
	l = [1, 1, 1, 1, 12, 2, 2, 2, 3, 4, 4, 5, 5]
	print(Counter(l))

	s = "assssjddkffggldfddaaaa"
	print(Counter(s))

	s = "How many times does each word show up in this sentence word word show up up"
	words = s.split()
	c = Counter(words)
	print(c)
	# Most common
	print(c.most_common(2))
	# Least common
	print(c.most_common()[:-2-1:-1])
	print(sum(c.values()))
	print(list(c))
	print(dict(c))
	print(set(c))
	# Clear a counter
	c.clear()
	print(c)

	