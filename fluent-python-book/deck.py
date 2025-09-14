import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class Deck:
    ranks = [str(n) for n in range(1, 11)] + 'JQKA'
    suits = 'clubs heart spades diamonds'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    def __getittem__(self, position):
        return self._cards[position]