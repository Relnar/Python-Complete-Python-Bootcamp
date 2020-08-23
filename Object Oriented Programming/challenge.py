
class BankAccount():
	def __init__(self, owner, balance):
		self.owner = owner
		self.balance = balance

	def deposit(self, amount):
		self.balance += amount
		print(f"Deposit of ${amount} accepted")

	def withdraw(self, amount):
		if amount > self.balance:
			print(f"Funds unavailable for ${amount}")
		else:
			self.balance -= min(amount, self.balance)
			print(f"Withdrawal of ${amount} accepted")

	def __str__(self):
		return f"{self.owner} = ${self.balance}"

def main():
	account = BankAccount("John", 1534.06)
	print(account)

	print("")
	account.deposit(111.0)
	print(account)

	print("")
	account.withdraw(5)
	print(account)

	print("")
	account.withdraw(5000)
	print(account)

if __name__ == "__main__":
	main()
