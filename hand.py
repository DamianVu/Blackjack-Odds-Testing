
class Hand:
	def __init__(self):
		self.cards = set()

	def value(self):
		# Value should only display the max value
		sum = 0
		aces = 0
		for card in self.cards:
			if card.card == "A":
				aces += 1
			else:
				sum += card.value()
		if aces > 0:
			sum += aces
			if sum < 12:
				sum += 10
		return sum

	def list(self):
		if (len(self.cards) == 0):
			print("[]")
		else:
			output = "["
			for card in self.cards:
				output = output + "\"" + card.card + " of " + card.suit + "\", "
			output = output[:-2]
			output = output + "]"
			print(output)

	def is_blackjack(self):
		return len(self.cards) == 2 and any(c.card == "A" for c in self.cards) and any(c.card == "10" or c.card == "J" or c.card == "Q" or c.card == "K" for c in self.cards)

	def has_ace(self):
		return any(c.card == "A" for c in self.cards)

	def can_be_split(self):
		temp = list(self.cards)
		return len(self.cards) == 2 and temp[0].card == temp[1].card

	def add(self, card):
		self.cards.add(card)
