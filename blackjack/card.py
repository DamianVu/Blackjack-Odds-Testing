
class Card:
	# Suit is defaulted to N/A so tests don't need to worry about suit
	def __init__(self, card, suit = "N/A"):
		self.card = card
		self.suit = suit

	def value(self):
		try:
			return int(self.card, 10)
		except ValueError:
			return 10
