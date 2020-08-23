def cool():
	def super_cool():
		return "I'm super cool"

	return super_cool

def hello():
	print("Hello")

def other(some_def_func):
	print("Other code runs here")
	some_def_func()

def new_decorator(original_func):

	def wrap_func():
		print("Some code before original function")
		original_func()
		print("Some code after original function")

	return wrap_func

# Shorten syntax to do the same as with new_decorator
@new_decorator
def hello_decorator():
	print("Hello decorator")

if __name__ == "__main__":
	some_func = cool()
	print("")

	print(some_func())
	print("")

	other(hello)
	print("")

	decorated_func = new_decorator(hello)
	decorated_func()
	print("")

	# Shorten syntax to do the same as with new_decorator
	hello_decorator()
