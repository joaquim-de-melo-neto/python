from main import Card

class Deck:
    '''Uma representação de um baralho de cartas com 52 cartas'''

    cards = []
    def __init__(self):
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        result = []
        for card in self.cards:
            result.append(str(card))
        return '\n'.join(result)
