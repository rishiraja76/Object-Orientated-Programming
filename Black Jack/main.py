#Importing package
import random

#Card declerations
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

#Class to create a card
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank + ' of ' + self.suit

#Class to create a deck of all cards
class Deck:
    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.deck = []
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.deck.append(Card(suit, rank)) # build Card objects and add them to the list
    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.deck)
    def deal(self):
        # Note we remove one card from the list of all_cards
        return self.deck.pop()

#Class to create a players han
class Hand:
    def __init__(self):
        # A new player has no cards
        self.cards = []
        self.value=0
        self.aces=0
    def add_card(self, card):
        self.cards.append(card)
        self.value=self.value+card.value
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces

    def adjust_for_ace(self):
        while self.value > 21 and self.aces>0:
            self.value -= 10
            self.aces -= 1

#Class to handle the chips a player has
class Chips:
    def __init__(self,total=100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0
    def win_bet(self):
        self.total=self.bet+self.total
    def lose_bet(self):
        self.total = self.total - self.bet

#Function to accept a bet value
def take_bet(chips,bet):
    if bet>chips.total:
        print("Bet greater than total")
    else:
        chips.bet=bet

#Function to add a card to the hand
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

#Function to ask the player to hit or stand
def hit_or_stand(deck, hand):
    choice=input("Do you want to hit? Y or N")
    if choice=="Y":
        hit(deck,hand)
        return choice
    else:
        return choice

#Function to print few of the crads in the hands of the dealer and all the crads with the player
def show_some(player, dealer):
    print("Dealer:")
    print(dealer.cards[0])
    print("Player:")
    for x in player.cards:
        print(x)

#Function to print all the cards in the hands of the dealer and player
def show_all(player, dealer):
    print("Dealer:")
    for x in dealer.cards:
        print(x)
    print("Player:")
    for x in player.cards:
        print(x)

#Function to check if the player busts
def player_busts(player,chips):
    if player.value > 21:
        chips.lose_bet()
        return True

#Function to check if player wins
def player_wins(player,dealer,chips):
    if player.value>dealer.value:
        chips.win_bet()
        return True

#Function to check if the dealer busts
def dealer_busts(dealer,chips):
    if dealer.value>21:
        chips.win_bet()
        return True

#Function to check if the dealer wins
def dealer_wins(player,dealer,chips):
    if dealer.value > player.value:
        chips.lose_bet()
        return True

#Function to check if its a draw
def push(player,dealer):
    if dealer.value==player.value:
        return True

while True:
    # Print an opening statement
    print("Welcome to BlackJack!")
    # Create & shuffle the deck, deal two cards to each player
    deck=Deck()
    deck.shuffle()
    player=Hand()
    dealer=Hand()
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())
    player.add_card(deck.deal())
    player.add_card(deck.deal())
    # Set up the Player's chips
    chips = Chips()
    # Prompt the Player for their bet
    bet=int(input("What bet would you like to place?"))
    take_bet(chips,bet)
    # Show cards (but keep one dealer card hidden)
    show_some(player,dealer)
    playing = True
    while playing:  # recall this variable from our hit_or_stand function
        # Prompt for Player to Hit or Stand
        choice=hit_or_stand(deck,player)
        # Show cards (but keep one dealer card hidden)
        show_some(player,dealer)
        while choice=="Y":
            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_busts(player,chips):
                print("Player bust! Dealer wins!")
                playing=False
                break
            else:
                choice=hit_or_stand(deck, player)
        else:
            # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
            while dealer.value < 17:
                hit(deck, dealer)
        # Show all cards
        show_all(player,dealer)
        # Run different winning scenarios
        if playing==False:
            break
        if dealer_busts(dealer, chips):
            print("Dealer bust! Player wins!")
            break
        elif player_wins(player,dealer,chips):
            print("Player wins!")
            break
        elif dealer_wins(player,dealer,chips):
            print("Dealer wins!")
            break
        elif push(player,dealer):
            print("Tie!")
            break
    # Inform Player of their chips total
    print("Total chips= {}".format(chips.total))
    # Ask to play again
    again=input("Play again? Y or N")
    if again=="Y":
        continue
    else:
        break
