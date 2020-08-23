def main():
	print("== Tuple unpacking ==")
	a = [(1, 2), (3 ,4)]
	for i,j in a:
		print(i)
		print(j)

	print("== List dictionary keys ==")
	d = {'k1':1, 'k2':2, 'k3':3 }
	for item in d:
		print(item)

	print("== List dictionary items ==")
	for key,value in d.items():
		print(key)
		print(value)

	print("== Loop where you don't care about the elements ==")
	for _ in d:
		print("Hello")

if __name__ == "__main__":
	main()

