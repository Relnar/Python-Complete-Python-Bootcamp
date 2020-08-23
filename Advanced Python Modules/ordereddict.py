from collections import OrderedDict

if __name__ == "__main__":
	# As of Python 3.7, insertion order is preserved for normal dictionary
	# Insertion order is not preserved in Python 2.x
	d = {}
	d['a'] = 1
	d['e'] = 5
	d['b'] = 2
	d['d'] = 4
	d['c'] = 3
	print(d)
	for k,v in d.items():
		print(k,v)
	print("")

	# The only reason to use OrderedDict is to make the code compatible with Python versions before 3.7
	# An OrderedDict preserve the insertion order, but it doesn't sort the keys.
	# See SortedDict for this purpose.
	orderedd = OrderedDict()
	orderedd['a'] = 1
	orderedd['e'] = 5
	orderedd['b'] = 2
	orderedd['d'] = 4
	orderedd['c'] = 3
	print(orderedd)
	for k,v in orderedd.items():
		print(k,v)
	print("")

	orderedd2 = OrderedDict()
	orderedd2['a'] = 1
	orderedd2['d'] = 4
	orderedd2['c'] = 3
	orderedd2['e'] = 5
	orderedd2['b'] = 2
	print(orderedd2)
	for k,v in orderedd2.items():
		print(k,v)
	print("")

	d2 = {}
	d2['a'] = 1
	d2['d'] = 4
	d2['c'] = 3
	d2['e'] = 5
	d2['b'] = 2
	print(d2)
	for k,v in d2.items():
		print(k,v)
	print("")

	print("dict equality doesn't check for insertion order")
	print(f"{d} == {d2}:", d == d2)
	print("")
	print("OrderedDict equality check for insertion order")
	print(f"{orderedd} == {orderedd2}:", orderedd == orderedd2)
