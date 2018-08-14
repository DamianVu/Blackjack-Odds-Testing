
class Hand:
	def __init__(self):
		self.cards = set()

	def value(self):
		sum = 0
		if any(c.card == "A" for c in self.cards):
			return "WE HAVE AN ACE"
		else:
			for card in self.cards:
				sum += card.value()
			return sum

	def add(self, card):
		self.cards.add(card)
