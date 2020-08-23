from collections import namedtuple

if __name__ == "__main__":
	t = (1, 2, 3)
	print(t)
	print("")

	# Create a class-like tuple
	Namedt = namedtuple('NamedTuple', 'k1 k2 k3 k4')
	# Instantiate this name tuple
	testnamedt = Namedt(k1=1, k2=2, k3=3, k4=4)
	print(testnamedt)
	print("testnamedt[0]:", testnamedt[0])
	print("testnamedt.k1:", testnamedt.k1)
