
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

	def has_ace(self):
		return any(c.card == "A" for c in self.cards)

	def can_be_split(self):
		temp = list(self.cards)
		return len(self.cards) == 2 and temp[0].card == temp[1].card

	def add(self, card):
		self.cards.add(card)
