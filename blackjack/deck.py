
import random
from card import Card

cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["Spades", "Clubs", "Diamonds", "Hearts"]

class Deck:
	def __init__(self,	deck_count):
		# Initializes the deck and adds a full set of cards
		self.deck_count = deck_count
		self.cards = []
		for i in range(deck_count):
			for c in cards:
				for s in suits:
					self.cards.append(Card(c, s))		

	def shuffle(self, shuffles = 1):
		# Shuffles deck X times or once by default
		for i in range(shuffles):
			random.shuffle(self.cards)

	def list(self):
		output = "["
		for card in self.cards:
			output = output + "\"" + card.card + " of " + card.suit + "\", "
		output = output[:-2]
		output = output + "]"
		return output

	def draw(self):
		return self.cards.pop()
