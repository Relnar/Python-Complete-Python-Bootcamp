from random import shuffle

class Card():
	def __init__(self, number):
		self.number = number
		self.revealed = False

	def __str__(self):
		return str(self.number)

class Deck():
	def __init__(self):
		self.cards = []

		for _ in range(0, 4):
			# Append ace has 11 value
			self.cards.append(Card(11))
			for card in range(2, 14):
				# Clamp the J, Q and K to 10
				self.cards.append(Card(min(card, 10)))

		shuffle(self.cards)

	def draw(self):
		return self.cards.pop() if len(self.cards) > 0 else None

class Hand():
	def __init__(self):
		self.cards = []
		self.revealCounter = 0

	def receiveCard(self, card):
		if card != None:
			self.cards.append(card)
			return True
		return False

	def revealCard(self):
		if self.revealCounter < len(self.cards):
			self.cards[self.revealCounter].revealed = True
			self.revealCounter += 1

	def validateHand(self):
		arraysum = 0
		arraysum = sum([card.number for card in self.cards if card.revealed])
		if arraysum <= 21:
			return arraysum
		else:
			numof11 = 0
			for card in self.cards:
				if card.number == 11:
					numof11 += 1
			if numof11 > 0:
				numof11 = max(1, numof11 - 1)
			arraysum -= 10 * numof11
			return arraysum

	def __str__(self):
		value = self.validateHand()
		string = ""
		for card in self.cards:
			string += str(card.number if card.number < 11 else 1) if card.revealed else "X"
			string += " "

		string += f" = {value}"
		if value > 21:
			string += " OVER!"
		return string

class Chip():
	def __init__(self, startingAmount):
		self.amount = startingAmount

	def bet(self):
		while True:
			try:
				betAmount = int(input("Bet some chips: "))
			except:
				print("Not a valid number")
			else:
				if betAmount <= 0:
					print(f"Invalid bet amount {betAmount}")
				elif betAmount <= self.amount:
					self.amount -= betAmount
					return betAmount
				else:
					print(f"Not enough chips for this bet")

	def receiveGain(self, betAmount):
		if betAmount > 0:
			self.amount += betAmount

	def __str__(self):
		return "Chip amount: " + str(self.amount)


if __name__ == "__main__":
	humanChips = Chip(100)

	while humanChips.amount > 0:
		deck = Deck()
		humanHand = Hand()
		dealerHand = Hand()

		print(humanChips)
		betAmount = humanChips.bet()
		print(humanChips)

		dealerHand.receiveCard(deck.draw())
		dealerHand.revealCard()
		dealerHand.receiveCard(deck.draw())
		print("Dealer hand: ", dealerHand)

		humanHand.receiveCard(deck.draw())
		humanHand.revealCard()
		humanHand.receiveCard(deck.draw())
		humanHand.revealCard()
		print("Your hand :", humanHand)

		humanHandValue = humanHand.validateHand()
		dealerHandValue = 0
		if humanHandValue < 21:
			while humanHandValue < 21:
				answer = input("Do you want to Hit another card (y/n)? ").lower()
				if answer == 'y':
					if humanHand.receiveCard(deck.draw()):
						humanHand.revealCard()
					else:
						print("Not enough cards")
						break

					print("Your hand :", humanHand)
					humanHandValue = humanHand.validateHand()
				elif answer == 'n':
					break
				else:
					print("Invalid input")

			dealerHand.revealCard()
			print("Dealer hand: ", dealerHand)
			dealerHandValue = dealerHand.validateHand()
			if humanHandValue <= 21:
				while dealerHandValue < humanHandValue:
					dealerHand.receiveCard(deck.draw())
					dealerHand.revealCard()
					print(dealerHand)
					dealerHandValue = dealerHand.validateHand()
		else:
			print("BLACKJACK !")

		if humanHandValue <= 21 and (humanHandValue > dealerHandValue or dealerHandValue > 21):
			print("You WIN!")
			humanChips.receiveGain(betAmount * 2)
		elif dealerHandValue == humanHandValue and dealerHandValue <= 21:
			print("Draw!")
			humanChips.receiveGain(betAmount)
		else:
			print("You LOSE!")

		del deck
		del humanHand
		del dealerHand

		if humanChips.amount > 0:
			playAgain = input("Play another hand (y/n)?").lower()
			if playAgain != 'y':
				break
		else:
			print("You're broke. See you !")
