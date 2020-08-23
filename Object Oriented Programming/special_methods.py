class Book():
	def __init__(self, title, author, pages):
		self.title = title
		self.author = author
		self.pages = pages

	# Special methods to convert a book to string
	def __str__(self):
		return f"{self.title} by {self.author}"

	# Special methods to return the length of a book
	def __len__(self):
		return self.pages

 	# Special methods to delete a book
	def __del__(self):
		print("A book object has been deleted")

def main():
	book = Book("Python rocks", "John", 200)
	print(book, ",", len(book), "pages")

	del book

if __name__ == "__main__":
	main()
