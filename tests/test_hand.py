
from blackjack.hand import Hand

def test_empty_hand():
	temp = Hand()
	assert temp.list() == "[]"
	assert temp.value() == 0


from blackjack.card import Card

# Value testing
def test_blackjack():
	temp = Hand()
	temp.add(Card("A"))
	temp.add(Card("K"))
	assert temp.is_blackjack()

def test_ace_calculation():
	temp = Hand()
	temp.add(Card("A"))
	assert temp.value() == 11
	temp.add(Card("A"))
	assert temp.value() == 12
	temp = Hand()
	temp.add(Card("9"))
	temp.add(Card("A"))
	assert temp.value() == 20
	temp.add(Card("A"))
	assert temp.value() == 21
	temp.add(Card("A"))
	assert temp.value() == 12

from blackjack.card_values import cards

def test_if_splits():
	# Test if we can split each duplicate hand
	for card in cards:
		temp = Hand()
		temp.add(Card(card))
		temp.add(Card(card))
		assert temp.can_be_split()

def test_splitting():
	# Test splitting each hand into two separate ones
	for card in cards:
		temp = Hand()
		temp.add(Card(card))
		temp.add(Card(card))

		first = Hand()
		second = Hand()
		first.add(temp.cards.pop())
		second.add(temp.cards.pop())
		assert first.value() == second.value()
		# Make sure split hand is empty
		assert len(temp.cards) == 0

