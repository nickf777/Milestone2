import random
suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
values = {'Two':2, 'Three':3, 'Four':4,'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace': 11}

playing = True

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    
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
    
    def add_card(self,new_cards):
        if type(new_cards) == type([]):
            self.cards.extend(new_cards)
        else:
            self.cards.append(new_cards)
        self.value = sum(self.cards)

    def adjust_for_ace(self):
        for card in self.cards:
            if card.rank == 'Ace':
                self.aces = self.value - 10


    def __str__(self):
        for card in self.cards:
            print(card)
        return 'This hand contains ' + str(len(self.cards)) + ' cards.'