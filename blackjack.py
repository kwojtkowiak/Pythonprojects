import random
# Version where Ace counts as a 10
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True

# Card class which creates a card


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

# Deck class with creates 52 unique cards


class Deck:
    def __init__(self):
        # Only happens when creating a new deck
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def __str__(self):
        deck_comp = " "  # start with empty string
        for card in self.all_cards:
            deck_comp += "\n" + card.__str__()
        return "The deck has " + deck_comp

    def shuffle(self):
        # It does not return anything
        random.shuffle(self.all_cards)

    def deal(self):
        # Removing one card from the list of all cards
        return self.all_cards.pop()

# Hand Class


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list
        self.value = 0  # start with 0 value of the hand
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        # card passed in is from class Deck (deal method is used) > single Card(suit,rank)
        self.cards.append(card)
        values[card.rank]  # to "unlock" dictionary provided at the start
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
    def __init__(self, total=100):
        self.total = total  # user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

# --------------------------------------------------FUNCTIONS--------------------------------------------------
# Ask the player for their bet, you can enter any name - it will be assigned to Chips class later


def take_bet(chips):

    while True:

        try:
            chips.bet = int(input("How many chips would you like to bet?: "))
        except:
            print("It's not a correct value!")
        else:
            if chips.bet > chips.total:
                print("Sorry, you do not have enough chips. You have: {}".format(chips.total))
            else:
                break
# Gives a player their next card


def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    while True:
        x = input("Do you want to [H]it or [S]tand?")
        if x == "H":
            hit(deck, hand)
        elif x == "S":
            print("Player Stands")
            playing = False
        else:
            print("It's not a valid answer! Enter H or S!")
            continue
        break


def show_some(player, dealer):

    # dealer.cards[1]

    # Show only ONE of the dealer's cards
    print("\nDealer's Hand: ")
    print("First card hidden!")
    print(dealer.cards[1])

    # Show all (2 cards) of the player's hand/cards
    print("\nPlayer's hand: ")
    for card in player.cards:
        print(card)


def show_all(player, dealer):

    # show all the dealer's cards
    # alternative would be print("\n Dealer's Hand: ",*dealer.cards,sep="\n")
    print("\n Dealer's Hand: ")
    for card in dealer.cards:
        print(card)

    # calculate and display value (J+K == 20)
    print(f"Value of Dealer's hand is: {dealer.value}")

    # show all the player's cards
    print("\n Player's hand: ")
    for card in player.cards:
        print(card)
    print(f"Value of Player's hand is: {player.value}")

# Ending the game


def player_busts(player, dealer, chips):
    print("Bust player!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Bust dealer!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()


def push(player, dealer):
    print("Dealer and player tie! PUSH")


# ------------------------------------------------------GAME LOGIC--------------------------------------------------------------------
while True:
    # Print an opening statement
    print("Welcome to Blackjack! A python exercise game made by Chris W.")
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_bank = Chips()
    # Prompt the Player for their bet
    take_bet(player_bank)
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)

    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_bank)
        
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:

        while dealer_hand.value < 17: #soft hit of casino
            hit(deck,dealer_hand)

        # Show all cards
        show_all(player_hand,dealer_hand)
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_bank)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_bank)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_bank)
        else:
            push(player_hand,dealer_hand)
    
    # Inform Player of their chips total
    print(f"\n Player total chips are at: {player_bank.total}")
    # Ask to play again
    new_game = input("Would you like to play again? y/n")

    if new_game[0].lower() == "y":
        playing = True
        continue
    else:
        print("Thank you for playing!")
        break
