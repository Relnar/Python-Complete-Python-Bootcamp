def main():
	my_list = ['STRING', 2, 3, 5, 9]
	my_list2 = [11, 22, 33]
	# Length
	print(len(my_list))
	print(my_list)
	# Skip elements like strings
	print(my_list[1:4:2])
	# Concatenation of 2 lists
	print(my_list + my_list2)
	# Mutable as opposed to strings
	my_list[2] = 'HELLO'
	print(my_list)
	# Insert in the list
	my_list.append('six')
	print(my_list)
	list3 = ['a', 'e', 'x', 'v', 'b']
	list4 = [3, 1, 6, 2]
	# Sorted in-place
	list3.sort()
	print(list3)


if __name__ == "__main__":
	main()

