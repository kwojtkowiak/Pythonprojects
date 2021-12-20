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
        

#Ask the player for their bet
