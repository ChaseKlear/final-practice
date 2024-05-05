"""
Question 1 (Classes):

Description:
Implement a "Card" class that represents a playing card in the average card game.
1) A Card, at minimum (you may add more as deemed necessary, but not remove), has the attributes:
    rank - integer representing the value of the card from 2-14
    suit - string represents the suit of a card
    name - string in the format `rank` of `suit`
    shorthand - string containing only the rank (int or first letter of rank) + fist letter of suit
2) Can be created given only a rank integer and a suit string, in that order
    suit string should be "Hearts", "Diamonds", "Clubs" or "Spades"
3) All attributes are private and have getter methods named `get_<attribute>` (e.g. `get_name`)
4) Cards can be printed in the format suit_color + shorthand + WHITE.
    suit_color should be RED for Hearts and Diamond suit cards, BLUE otherwise
5) Cards can be compared for equality using their rank and suit
6) Cards can be added to a set or dictionary
7) Cards can be sorted by their suit and then rank
    Their suit should in the order of Clubs -> Hearts -> Spades -> Diamonds
    Rank should be from least to greatest

You may assume any inputs are valid therefore you do not need to implement error checking.

NOTE: The provided constants are to make the problem easier, please make use of them.
SUIT_KEY_VALUE can be helpful for implementing how a card can be sorted by suit and rank.
"""

# Provided ANSI color strings
RED = '\u001b[31;1m'
BLUE = '\u001b[36;1m'
WHITE = '\u001b[0m'
# Anything printed after RED or BLUE will be in that color until you print WHITE

# Provided rank to name dictionary for ranks above 10
RANK_TO_NAME = {11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}
SUIT_KEY_VALUE = {'Clubs': 1, 'Hearts': 2, 'Spades': 3, 'Diamonds': 4}

class Card:
    __slots__ = ["__rank", "__suit", "__name", "__shorthand"]
    def __init__(self, rank:int, suit:str):
        self.__rank = rank
        self.__suit = suit
        if rank <= 10:
            self.__name = str(rank) + " of " + suit
            self.__shorthand = str(rank) + suit[0]
        else:
            self.__name = str(RANK_TO_NAME[rank]) + " of " + suit
            self.__shorthand = str(RANK_TO_NAME[rank])[0] + suit[0]
        
    def get_rank(self):
        return self.__rank
    def get_suit(self):
        return self.__suit
    def get_name(self):
        return self.__name
    def get_shorthand(self):
        return self.__shorthand
    
    def __lt__(self, other:object):
        if isinstance(other, Card):
            if self.__suit == other.__suit:
                return self.__rank < other.__rank
            return SUIT_KEY_VALUE[self.__suit] < SUIT_KEY_VALUE[other.__suit]
        return None
    
    def __eq__(self, other):
        if isinstance(other, Card):
            return self.__name == other.__name
        return None
    
    def __hash__(self):
        return hash(self.__name)
    
    def __repr__(self):
        if self.__suit == "Clubs" or self.__suit == "Spades":
            return BLUE + self.__shorthand + WHITE
        return RED + self.__shorthand + WHITE