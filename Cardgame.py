from random import shuffle
from time import sleep

# 21 game. It takes 1 player and 1 dealer. they each get 3 cards. the sum of the 3 cards is checked to see =21
# Player is able to hit (gain another card if the original card sum way less than 21) or stay (close to 21)
# Dealer is unable to hit/stay. only able to take their own 3 cards.
# Maybe try implementing a chip system. that could be cool

# Deck. Numeric only, for now.
cards = []
for i in range(2, 14):
    shuffle(cards)
    cards.append(i)


# Player hand. Contains the cards as well as unique actions for the player.
def player_hand():
    p_card1 = cards[0]
    p_card2 = cards[1]
    p_card3 = cards[2]
    print('For this round, your cards are: {}, {}, {} .'.format(p_card1, p_card2, p_card3))
    sum1 = p_card1 + p_card2 + p_card3
    print("The sum of your cards is " + str(sum1) + '.')
    return

# Initial sum of cards
def initial_sum():
    return cards[0] + cards[1] + cards[2]

# Action is unique to players.
def p_hit():
    return cards[10] + cards[0] + cards[1] + cards[2]



# Dealer hand
def dealer_hand():
    d_card1 = cards[3]
    d_card2 = cards[4]
    d_card3 = cards[5]
    print('For this round, the dealer had: {}, {}, {} '.format(d_card1, d_card2, d_card3))
    card_sum = d_card1 + d_card2 + d_card3
    print("The dealer had " + str(card_sum) + " in total.")
    return


# Game state. Contains the logic/flowchart of the game

def game():
    print("Welcome. Try to get the sum of your cards to 21")
    player_hand()
    if initial_sum() > 21:
        sleep(2.5)
        print('Its a bust! Game over.')
        dealer_hand()


    elif initial_sum() == 21:
        sleep(2.5)
        print('You win!')
        dealer_hand()


    else:
        a = input("Would you like to hit or fold?")

        if a == 'hit':
            print('The new card is: ' + str(cards[10]))
            print('The new sum is: ' + str(p_hit()))
            sleep(2.5)
            if p_hit() > 21:
                print('Its a bust! Game over.')
                dealer_hand()
            elif p_hit() < 21:
                print('Would you like to hit again or fold')
            elif p_hit() == 21:
                print('You win!')
                dealer_hand()

        else:
            sleep(3)
            print('Game over.')
            return dealer_hand()


game()


#TEST 2
#DID IT WORK?
