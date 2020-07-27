import random
suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
values = {'Two':2, 'Three':3, 'Four':4,'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace': 11}

playing = True

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
    
    def __str__(self):
        for card in self.all_cards:
            print(card)
        return 'There are ' + str(len(self.all_cards)) + ' cards left in the deck.'
        
    
    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal(self):
        return self.all_cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self,card):
        #should call deal from the deck class
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


    def __str__(self):
        for card in self.cards:
            print(card)
        return 'This hand contains ' + str(len(self.cards)) + ' cards.'

class Chips:
    def __init__(self,total=100):
        self.total = total
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
    
    def __str__(self):
        return 'You currently have $' + str(self.total) + 'in chips.'

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet'))
        except:
            print('Sorry! Please put in an integer.')
        else:
            if chips.bet > chips.total:
                print(f'Sorry! You do not have enough chips for this bet. You have {chips.total} chips.')
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace

def hit_or_stand(deck,hand):
    global playing
    
    while True:
        choice = input('Do you want to hit? (Y/N)')
        if choice[0].upper() == 'Y':
            print('You have chosen to hit.')
            hit(deck,hand)
        elif choice[0].upper() == 'N':
            print("Player Stands. Dealer's Turn!")
            playing = False
        else:
            print('Sorry I do not understand. Please enter Y or N.')
        break
    

def show_some(player,dealer):
    #The dealer's first card is visible and all the player's cards are visible. 
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

def show_all(player,dealer):
    #At the end all cards are visible
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(player,dealer,chips):
    print('Player busts')
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('Player wins!')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('Dealer busts!')
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print('Dealer wins!')
    chips.lose_bet()

def push(player,dealer,chips):
    print('Dealer and player tie!')

#Game Logic

while True:
    print('Hello and welcome to Blackjack!')

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand,dealer_hand)

    while playing:
        hit_or_stand(deck,player_hand)

        show_some(player_hand,dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)

            break
    
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

        show_all(player_hand,dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand,player_chips)
        
    print(f'\n Player total chips are at {player_chips.total}')

    new_game = input('Would you like to play a new game? (Y/N)')

    if new_game[0].upper() == 'Y':
        playing = True
    else:
        print('Thank you for playing!')
        break