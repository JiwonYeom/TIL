# Python Card Deck
import collections
Card = collections.namedtuple('Card', ['rank','suit'])

class FrenchDeck:
    # construct simple class to represent individual cards
    # From python 2.6, namedtuple can be used to build classes of objects(bundles of attributes with no custom methods, like a database record)

    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hards'.split()

    # initiate `_cards` when object is created. This local var is only used internally
    def __init__(self):
        self._cards = [Card(rank,suit)] for suit in self.suits for rank in self.ranks]

    # overrides len() python method
    def __len__(self):
        return len(self._cards)
    
    # get method
    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()

len(deck) # 52
deck[0] # Card(rank='2', suit='spades') => also triggers __getitem__
deck[-1] # Card(rank='A', suit='hearts')

# trying to make a method to choose random card
# random is standard library
from random import choice

choice(deck) # randomly picks card

deck[:3] # lists first 3 cards
deck[12::13]  # start at index 12, skip 13 cards at a time
# [Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'),Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]

Card('Q', 'hearts') in deck # True

# to sort, 
# create dict
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]