
# The decision function will return a string with the action we should
# take according to basic strategy.
# Required arguments are the players hand then the dealers hand.
# Optional arguments are different rules the dealer follows.

# Dictionary[player_value][computer_value] = Decision


def decision(player_hand, dealer_hand, dealer_hits_soft_17 = True, double_after_split = False, surrenders = False):
    if player_hand.can_be_split():

    if player_hand.is_soft_value():

    # Otherwise, we have some hard value
