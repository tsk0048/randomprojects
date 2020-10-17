import random
from time import sleep

# 21 game. It takes 1 player and 1 dealer. they each get 3 cards. the sum of the 3 cards is checked to see =21
# Player is able to hit (gain another card if the original card sum way less than 21) or stay (close to 21)
# Dealer is unable to hit/stay. only able to take their own 3 cards.
# Maybe try implementing a chip system. that could be cool

# Deck. Numeric only, for now.
# This branch will try out randint instead of actual cards
player_card = {"p_card1":1, "p_card2":1, "p_card3":1}
def shuffle():
    a = random.randint(2,14)
    b = random.randint(2,14)
    c = random.randint(2,14)
    return player_card.update({"p_card1":a}) , player_card.update({"p_card2":b}) , player_card.update({"p_card3":c})

# Player hand. Contains the cards as well as unique actions for the player.
def player_hand():
    card_1 = player_card.get("p_card1")
    card_2 = player_card.get("p_card2")
    card_3 = player_card.get("p_card3")
    print('For this round, your cards are: {}, {}, {} .'.format(card_1, card_2, card_3))
    sum1 = card_1 + card_2 + card_3
    print("The sum of your cards is " + str(sum1) + '.')
    return

# Initial sum of cards
def initial_sum():
    return p_card1 + p_card2 + p_card3

# Action is unique to players.
def p_hit():
    return p_card1 + p_card2 + p_card3



# Dealer hand
d_card1 = random.randint(2, 14)
d_card2 = random.randint(2, 14)
d_card3 = random.randint(2, 14)

def dealer_hand():
    print('For this round, the dealer had: {}, {}, {} '.format(d_card1, d_card2, d_card3))
    card_sum = d_card1 + d_card2 + d_card3
    print("The dealer had " + str(card_sum) + " in total.")
    return


# Game state. Contains the logic/flowchart of the game

def game():
    while True:
        print("Welcome. Try to get the sum of your cards to 21")
        player_hand()
        if initial_sum() > 21:
            sleep(2.5)
            print('Its a bust! Game over.')
            dealer_hand()
            if input('Would you like to play again?') in ('Yes' , 'y' , 'yes'):
                return game()
            else:
                break


        elif initial_sum() == 21:
            sleep(2.5)
            print('You win!')
            dealer_hand()
            if input('Would you like to play again?') in ('Yes', 'y', 'yes'):
                return game()
            else:
                break



        else:
            a = input("Would you like to hit or fold?")

            if a == 'hit':
                print('The new card is: ' + str(random.randint(2, 14)))
                print('The new sum is: ' + str(p_hit()))
                sleep(2.5)
                if p_hit() > 21:
                    print('Its a bust! Game over.')
                    dealer_hand()
                    if input('Would you like to play again?') in ('Yes', 'y', 'yes'):
                        return game()
                    else:
                        break
            elif p_hit() < 21:
                if input('Would you like to hit ') == 'Yes':
                    return p_hit()
                if input('Would you like to fold') == 'No':
                    return game()

            elif p_hit() == 21:
                print('You win!')
                dealer_hand()
                if input('Would you like to play again?') in ('Yes', 'y', 'yes'):
                    return game()
                else:
                    break

            else:
                sleep(3)
                print('Game over.')
                return dealer_hand()
            if input('Would you like to play again?') in ('Yes', 'y', 'yes'):
                return game()
            else:
                break
game()