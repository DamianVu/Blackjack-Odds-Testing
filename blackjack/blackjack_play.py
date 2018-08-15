
from blackjack.deck import Deck
from blackjack.hand import Hand


def play():
	print("Welcome to blackjack!\n=====================")

	print("Number of decks?")
	try:
		num_decks = int(input(), 10)
	except ValueError:
		print("You need to give me an integer value!")
		return
	print("Starting cash?")
	try:
		cash = int(input(), 10)
	except ValueError:
		print("You need to give me an integer value!")
		return
	deck = Deck(num_decks)
	deck.shuffle(20)

	print("Let's Play!")
	while cash > 0 and len(deck.cards) > num_decks * 16:
		print("Your cash: $" + str(cash))
		print("Place your bet!:")
		try:
			bet = int(input(), 10)
		except ValueError:
			print("You need to give me an integer value!")
			return
		player_hand = Hand()
		dealer_hand = Hand()
		player_hand.add(deck.draw())
		dealer_hand.add(deck.draw())
		player_hand.add(deck.draw())
		playing = 1
		player_bust = 0
		player_blackjack = 0
		while playing:
			print()
			print("Dealer shows: " + dealer_hand.list())
			print("Your hand: " + player_hand.list())
			print("Your current value: " + str(player_hand.value()))
			print()
			if player_hand.is_blackjack():
				player_blackjack = 1
				print("B L A C K J A C K !")
				break
			if player_hand.value() > 21:
				player_bust = 1
				print("You bust!")
				break
			print("Pick an action:")
			print("- (h)it")
			print("- (s)tay")
			if player_hand.can_be_split():
				print("- S(p)lit")
			action = input()
			if action == "h":
				player_hand.add(deck.draw())
			elif action == "s":
				playing = 0

		if player_blackjack:
			cash += bet
			print("You win!")
			continue

		if player_bust:
			print("Dealer wins!")
			cash -= bet
			continue

		dealer_is_playing = 1
		dealer_bust = 0
		while dealer_is_playing:
			print("Dealer: " + dealer_hand.list() + ", Value: " + str(dealer_hand.value()))
			if dealer_hand.value() < 17:
				print("Dealer hits!")
				dealer_hand.add(deck.draw())
			elif dealer_hand.value() > 21:
				print("Dealer busts!")
				dealer_bust = 1
				break
			elif dealer_hand.value() == 17 and dealer_hand.has_ace():
				print("Dealer hits!")
				dealer_hand.add(deck.draw())
			else:
				dealer_is_playing = 0

		print("Result:")
		print("Dealer hand: " + dealer_hand.list() + ", Value: " + str(dealer_hand.value()))
		print("Your hand: " + player_hand.list() + ", Value: " + str(player_hand.value()))

		if dealer_bust or player_hand.value() > dealer_hand.value():
			print("You win $" + str(bet) + "!")
			cash += bet
		elif player_hand.value() < dealer_hand.value():
			print("You lose!")
			cash -= bet
		else:
			print("PUSH!")
