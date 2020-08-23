import timeit

if __name__ == "__main__":
	t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
	print("Time:", t)
	print("")

	print("Timing list comprehension")
	t = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
	print("Time:", t)
	print("")

	print("Timing map function")
	t = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
	print("Time:", t)

