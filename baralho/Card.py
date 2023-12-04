class Card:
    '''Uma representação d ecartas do baralho'''

    suits = ['paus', 'ouro', 'espadas', 'copas']
    ranks = [None, 'Ás', 'Dois', 'Três', 'Quatro',
             'Cinco', 'seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Valete', 'Rainha', 'Rei']
    def __init__(self,suit = 0, rank = 2):
        self.suit = suit
        self.rank = rank

    def __lt__(self, other):
        tupla1 = self.suit, self.rank
        tupla2 = other.suit, other.rank
        return tupla1 < tupla2

    def __str__(self):
        return '%s de %s' % (Card.ranks[self.rank],Card.suits[self.suit])
