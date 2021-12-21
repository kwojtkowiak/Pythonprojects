import random
#Version where Ace counts as a 10
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

#Card class which creates a card
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

#Deck class with creates 52 unique cards
class Deck:
    def __init__(self):
        #Only happens when creating a new deck
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = " " #start with empty string
        for card in self.all_cards:
            deck_comp += "\n"+ card.__str__()
        return "The deck has "+ deck_comp
    
    def shuffle(self):
        #It does not return anything
        random.shuffle(self.all_cards)

    def deal(self):
        #Removing one card from the list of all cards
        return self.all_cards.pop()
        
#Hand Class
class Hand:
    def __init__(self):
        self.cards = [] #start with an empty list
        self.value = 0 #start with 0 value of the hand
        self.aces = 0 # add an attribute to keep track of aces
    
    def add_card(self,card):
        #card passed in is from class Deck (deal method is used) > single Card(suit,rank)
        self.cards.append(card)
        values[card.rank]
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1
    
    def adjust_for_ace(self):
        # If total value > 21 and I still have an ace 
        # than change my ace to be a 1 instead of an 11
        # no values for self.aces because it's considered as boolean value (sefl.aces > 0 == self.aces)
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self,total=100):
        self.total = total #user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet

#Ask the player for their bet, you can enter any name - it will be assigned to Chips class earlier
def take_bet(chips):

    while True:

        try:
            chips.bet = int(input("Please enter your bet: "))
        except:
            print("It's not a correct value!")
        else:
            if chips.bet > chips.total: 
                print("Sorry, you do not have enough chips. You have: {}".format(chips.total))
            else:
                break
