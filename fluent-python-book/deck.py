import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class Deck:
    ranks = [str(n)] + 'JQKA'