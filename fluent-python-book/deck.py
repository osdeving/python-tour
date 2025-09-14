import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class Deck:
    ranks = [str(n) for n in range(1, 11)] + 'JQKA'
    suits = ''