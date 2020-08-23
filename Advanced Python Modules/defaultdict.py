from collections import defaultdict

if __name__ == "__main__":
	d = { 'k1' : 1 }
	print(f"Normal dictionary {d}")
	print(d['k1'])
	try:
		print(d['k2'])
	except:
		print("Error d['k2'] not found")
	print("")

	print("Initialize defaultdict with a default object")
	defaultd = defaultdict(object)
	print("Empty defaultd ")
	print("")
	print(defaultd)
	print("")
	print("Accessing invalid key defaultd['one']")
	defaultd['one']
	print(f"Created defaults for defaultd: {defaultd}")
	print("")

	print("Initialize defaultdict with a lambda function that always return 0")
	d = defaultdict(lambda: 0)
	d['one']
	d['two']
	print(f"Created defaults for d: {d}")
	print("")
