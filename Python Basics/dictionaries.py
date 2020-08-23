import copy

def main():
	# Dictionaries can't be sorted
	my_dict = {'key1':'value1', 'key2':['value2', 'value3']}
	print(my_dict)
	print(my_dict['key1'])

	# Add element
	my_dict['price'] = 2.99
	print(my_dict)

	# List keys
	print(my_dict.keys())
	print(my_dict.values())
	print(my_dict.items())

	# Shallow copy (reference)
	my_dict2 = my_dict

	# Deep copy
	my_dict3 = copy.deepcopy(my_dict)

	# Delete element
	del my_dict['key2']
	print("Delete item:")
	print("Original", my_dict)
	print("Shallow copy", my_dict2)
	print("Deep copy", my_dict3)


if __name__ == "__main__":
	main()

