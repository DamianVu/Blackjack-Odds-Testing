
import random
from card import Card

cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["Spades", "Clubs", "Diamonds", "Hearts"]

class Deck:
	def __init__(self,	deck_count):
		self.deck_count = deck_count
		self.cards = []
		for i in range(deck_count):
			self.add_deck()

	def shuffle(self):
		random.shuffle(self.cards)

	def add_deck(self):
		for c in cards:
			for s in suits:
				self.cards.append(Card(c, s))

	def list(self):
		output = "["
		for card in self.cards:
			output = output + "\"" + card.card + " of " + card.suit + "\", "
		output = output[:-2]
		output = output + "]"
		print(output)
