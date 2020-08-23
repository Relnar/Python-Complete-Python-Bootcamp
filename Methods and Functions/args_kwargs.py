# args is just a name, the important part for variable arguments is the *
def myfunc_args(*args):
	print("sum of", args)
	return sum(args)

# kwargs is just a name, the important part for variable arguments is the **
def myfunc_kwargs(**kwargs):
	print("sum of", kwargs)
	return sum(kwargs.values())

def myfunc_args_kwargs(*args, **kwargs):
	print("sum of", args, "and", kwargs)
	return sum(kwargs.values()) + sum(args)


def main():
	print("== *args ==")
	print(myfunc_args(1))
	print(myfunc_args(1, 2, 3, 4))

	print("== **kwargs ==")
	print(myfunc_kwargs(key = 1))
	print(myfunc_kwargs(key1 = 1, key2 = 2, key3 = 3))

	print("== (*args, **kwargs) ==")
	print(myfunc_args_kwargs(1, 2, 3, key1 = 4, key2 = 5, key3 = 6))

if __name__ == "__main__":
	main()
