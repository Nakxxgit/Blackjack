import random
import score

#define deck
class Deck():
    def __init__(self):
        self.card_list=list()

    def deck_generator(self):
        suits=['Heart', 'Diamond', 'Club', 'Spade']
        cards=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'Q', 'J', 'Ace']
        for suit in suits:
            for card in cards:
                self.card_list.append([suit, card])

        random.shuffle(self.card_list)

    #get one card from deck
    def get_card(self):
        return self.card_list.pop()

#define player
class player():
    def __init__(self, player_deck: list, money= None, score= None):

        if money is None:
            self.money=100
        else:
            self.money=money

        if score is None:
            self.score=0

        self.player_deck = player_deck

    def hit(self, new_card: list):
        self.player_deck.append(new_card)

    def stand(self):
        return score.get_score(self.player_deck)

    def display_player_deck(self):
        print ("You have: ", end='')
        for c in self.player_deck:
            print (c, end='\t')

    def check_lose(self):
        if score.get_score(self.player_deck)>21:
            return True
        return False

def start(player, dealer_value, deck):
    print ("You have: £%s " %(player.money))
    print ("1.bet   2.quit")

    while choice1 in ['1', '2']:
        choice1=input()
    bet=0
    if choice1=='1':
        while bet not in [10, 20, 30]:
            bet=int(input("Choose bet money(10, 20, 30):    "))
            if bet>player.money:
                print ("You can't bet more money than you have")
                bet=0
        print ("Choose bet money: ", bet)

    if choice1=='2':
        print ("Quit game")
        quit()
#infinite loop(as occur every turn)
    while True:
        player.display_player_deck()
        player.score=player.stand()
        print ("Your score is: %s" %(player.score))

        print ("1. hit  2.stand")
        choice2=input()
        if choice2=='1':#choice=hit
            player.hit(deck.get_card())

            if player.check_lose():#player lose
                player.display_player_deck()
                print ("Your score is : %s" %(player.stand()))
                print ("You lose! You lose your bet money.")
                player.money-=bet
                return player.money

        if choice2=='2':#choice=stand
            if player.stand()<dealer_value and dealer_value<=21:#player lose
                print ("dealer value: %s" %(dealer_value))
                print ("Your total value: %s" %(player.stand()))
                print ("You lose!")
                print ("You lose your bet money.")
                player.money-=bet
                return player.money

            elif player.stand==dealer_value:
                print("dealer value: %s" % (dealer_value))
                print("Your total value: %s" % (player.stand()))
                print("You draw")
                print("You do not lose and earn money.")

            elif dealer_value>21:#dealer lose
                print("dealer value: %s" % (dealer_value))
                print("Your total value: %s" % (player.stand()))
                print ("You win! you get bet money.")
                player.money+=bet
                return player.money

            else:#player win
                print ("dealer value: %s" % (dealer_value))
                print ("Your total value: %s" % (player.stand()))
                print ("You win!")
                print ("You get bet money")
                player.money+=bet
                return player.money
