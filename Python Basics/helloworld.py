

def main():
	x = "hello world"
	y=112.123456
	print(x.upper())
	print(x)
	print(x.split())
	print(x.split("o"))
	print("Test format {}".format(y))
	print("Test format {1} {0}".format(x, y))
	print("Test format {b:1.2} {f}".format(f=x, b=y))
	print("Test format {b:2.2f} {f}".format(f=x, b=y))
	print("Test format {b:.2f} {f}".format(f=x, b=y))
	print(f"Test format {x} {y:.2f}")


if __name__ == "__main__":
	main()

