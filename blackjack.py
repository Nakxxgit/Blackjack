#import scripts that I made, and import random
import game
import score
import random

#define rule
def rule():
    print ('') #make a space
    with open('rule.txt', 'r') as f:
        print (f.read())
    print ("\nWrite down any words then game is started")
    input()
    return

if __name__=="__main__":
    print ("Welcome to the blackjack! Do you want to see the rule? (y/n)")
    rule_choice=str()
    possible_input=['y', 'yes', 'n', 'no']

    while rule_choice not in possible_input:
        rule_choice=input()
        if rule_choice in ['yes', 'y']:
            rule()
            break
        if rule_choice in ['no', 'n']:
            break

    deck=game.Deck() #bring deck(class) from game module
    deck.deck_generator() #make cards
    dealer_database=range(17, 24)  #make dealerdatabase
    dealer_value=random.choice(dealer_database)#get dealer value
    player=game.player([deck.get_card() for i in range(2)]) #get two cards

    while True: #infinite loop to play game
        print ("\n Let's start new game.")
        save=game.start(player, dealer_value, deck)
        if player.money<=0: #player lose all money that he has->finish game
            print ("You lose all money. Finish game. Thank you for enjoying.")
            break

        #make new deck
        deck=game.Deck()
        deck.deck_generator()

        #After the game, give update money to saved, make new player card and dealer value to prepare next game
        player=game.player([deck.get_card() for i in range(2)], save)
        dealer_value=random.choice(dealer_database)
