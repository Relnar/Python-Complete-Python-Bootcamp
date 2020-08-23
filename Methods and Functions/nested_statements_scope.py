name = "Global"

def function():
	name = "Local"

	def enclosingfunc():
		name = "E: Enclosing function local"
		return name
	
	print(enclosingfunc())
	return name

def globalredefinition():
	global name
	name = "Global redefinition"

def main():
	# LEGB Rule:
	# - L: Local
	# - E: Enclosing function local
	# - G: Global (module)
	# - B: Built-in (Python)
	print("L: " + function())
	print("G: " + name)
	print("B: " + __name__)
	globalredefinition()
	print("G redefinition: " + name)

if __name__ == "__main__":
	main()
