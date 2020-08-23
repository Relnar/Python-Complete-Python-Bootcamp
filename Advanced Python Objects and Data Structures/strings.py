
if __name__ == "__main__":
	s = "hello world"
	print(s)
	print(f"capitalize: {s.capitalize()}")
	print(f"upper: {s.upper()}")
	print(f"title: {s.title()}")
	print(f"lower: {s.lower()}")
	print(f"count('o'): {s.count('o')}")
	print(f"find('o'): {s.find('o')}")
	print(f"center(20,'z'): {s.center(20, 'z')}")
	print(f"tab: hello\tworld")
	print("")

	s = "hihihihiiihhihii"
	print(f"s = {s}")
	print(f"isalnum: {s.isalnum()}")
	print(f"isalpha: {s.isalpha()}")
	print(f"islower: {s.islower()}")
	print(f"isupper: {s.isupper()}")
	print(f"isspace: {s.isspace()}")
	print(f"istitle: {s.istitle()}")
	print(f"s[-1] (wrap around): {s[-1]}")
	print(f"split('i'): {s.split('i')}")
	print(f"partition('i): {s.partition('i')}")
