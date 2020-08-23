from random import shuffle
from random import randint

def main():
	print("== list comprehensions ==")
	mystring = "hello"
	mylist = [letter for letter in mystring]
	print(mylist)

	print("even number at power of 2")
	mylist = [num**2 for num in range(0, 11, 2)]
	print(mylist)

	print("every 3 numbers using if statement")
	mylist = [num for num in range(0, 11) if num%3==0]
	print(mylist)

	print("with else statement (order declaration is reversed")
	# Order is reverse with an else statement
	results = [x if x%2==0 else 'ODD' for x in range(0, 11)]
	print(results)

	print("convert from celcius to fahrenheit")
	celcius = [0, 10, 20, 34.5]
	fahrenheit = [((9.0/5.0)*temp + 32) for temp in celcius]
	print(celcius, " to ", fahrenheit)

	print("nested loops")
	mylist = [x*y for x in [2,4,6] for y in [1,10,1000]]
	print(mylist)

if __name__ == "__main__":
	main()
