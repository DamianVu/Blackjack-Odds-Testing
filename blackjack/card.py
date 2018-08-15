
class Card:
	def __init__(self, card, suit):
		self.card = card
		self.suit = suit

	def value(self):
		try:
			return int(self.card, 10)
		except ValueError:
			return 10
