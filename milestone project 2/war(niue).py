import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
#Card class
class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank + " of " + self.suit
#Deck class
class Deck:

    def __init__(self): #tworzy nowy deck
        self.all_cards = [] #lista ktora jest wypelniania wszystkimi kartami z talii

        for suit in suits: #4 kolory
            for rank in ranks: #wszystkie rangi
                #Create the Card Object
                created_card = Card(suit,rank) #tworzy unikalna karte > "for" loop
                self.all_cards.append(created_card) 
    # przetasowanie
    
    def shuffle(self):

        random.shuffle(self.all_cards)
    
    #wybranie karty, do uzycia na potem

    def deal_one(self):
        return self.all_cards.pop()

#Player class
class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0) #pop = 0 zeby zawsze usuwal "z wierzchu"
    def add_cards(self):
        if type(new_cards) == type([]):
            #lista, kilka kart
            self.all_cards.extend(new_cards)
        else:
            #jedna karta
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

#Game setup
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one)
    player_two.add_cards(new_deck.deal_one)

game_on = True

round_num = 0
while game_on:
    round_num += 1
    print(f'Round {round_num}')

    if len(player_one.all_cards) == 0:
        print("Player One, out of cards. Player Two wins!")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player Two, out of cards. Player One wins!")
        game_on = False
        break

#start a new round
player_one_cards = []
player_one_cards.append(player_one.remove_one())
player_two_cards = []
player_two_cards.append(player_two.remove_one())

#while at_war
at_war = True

while at_war:

    if player_one_cards[-1].value > player_two_cards[-1].value:

        player_one.add_cards(player_one_cards)
        player_one.add_cards(player_two_cards)
        at_war = False
    
    elif player_one_cards[-1].value < player_two_cards[-1].value:

        player_two.add_cards(player_one_cards)
        player_two.add_cards(player_two_cards)
        at_war = False

    else: 
        print("WAR!")

        if len(player_one.all_cards) < 3:
            print("Player One unable to declare war")
            print("Player Two Wins!")
            game_on = False
            break

        elif len(player_two.all_cards) < 3:
            print("Player Two unable to declare war")
            print("Player One Wins!")
            game_on = False
            break

        else:
            for num in range(3):
                player_one_cards.append(player_one.remove_one())
                player_two_cards.append(player_two.remove_one())