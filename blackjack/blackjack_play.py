
from blackjack.deck import Deck
from blackjack.hand import Hand


def play():
    print("Welcome to blackjack!\n=====================")

    try:
        num_decks = int(input("Number of decks?: "), 10)
    except ValueError:
        print("You need to give me an integer value!")
        return
    try:
        cash = int(input("Starting cash?: "), 10)
    except ValueError:
        print("You need to give me an integer value!")
        return
    deck = Deck(num_decks)
    deck.shuffle(20)

    times_won = 0
    times_drawn = 0
    times_lost = 0

    print("Let's Play!")
    while cash > 0 and len(deck.cards) > num_decks * 16:
        print(f"Your cash: ${cash}")
        try:
            bet = int(input("Place your bet!: "), 10)
        except ValueError:
            print("You need to give me an integer value!")
            break
        player_hand = Hand()
        dealer_hand = Hand()
        player_hand.add(deck.draw())
        dealer_hand.add(deck.draw())
        player_hand.add(deck.draw())
        player_bust = False
        player_blackjack = False
        while True:
            print()
            print(f"Dealer shows: {dealer_hand.list()}")
            print(f"Your hand: {player_hand.list()}")
            print(f"Your current value: {player_hand.value()}")
            print()
            if player_hand.is_blackjack():
                player_blackjack = True
                print("B L A C K J A C K !")
                break
            if player_hand.value() > 21:
                player_bust = True
                print("You bust!")
                break
            print("Options")
            print("=======")
            print("- (h)it")
            print("- (s)tay")
            if player_hand.can_be_split():
                print("- S(p)lit")
            action = input("Pick an action: ")
            if action == "h":
                player_hand.add(deck.draw())
            elif action == "s":
                break

        if player_blackjack:
            cash += bet
            print("You win!")
            times_won += 1
            continue

        if player_bust:
            print("Dealer wins!")
            cash -= bet
            times_lost += 1
            continue

        dealer_bust = False
        while True:
            print(f"Dealer: {dealer_hand.list()} Value: {dealer_hand.value()}")
            if dealer_hand.value() < 17:
                print("Dealer hits!")
                dealer_hand.add(deck.draw())
            elif dealer_hand.value() > 21:
                print("Dealer busts!")
                dealer_bust = True
                break
            elif dealer_hand.value() == 17 and dealer_hand.has_ace():
                print("Dealer hits!")
                dealer_hand.add(deck.draw())
            else:
                break
        print()
        print("Result:")
        print(f"Dealer hand: {dealer_hand.list()}, Value: {dealer_hand.value()}")
        print(f"Your hand: {player_hand.list()}, Value: {player_hand.value()}")

        if dealer_bust or player_hand.value() > dealer_hand.value():
            print(f"You win ${bet}!")
            times_won += 1
            cash += bet
        elif player_hand.value() < dealer_hand.value():
            print("You lose!")
            times_lost += 1
            cash -= bet
        else:
            print("PUSH!")
            times_drawn += 1
    print("Thanks for playing!")
    print(f"You won {times_won} hands.")
    print(f"You lost {times_lost} hands.")
    print(f"You pushed {times_drawn} hands.")
