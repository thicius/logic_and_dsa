# Escrever um método dentro de um Deck que deixe as cartas em ordem crescente:


class Card:

    def __init__(self, suit=0, rank=2) -> None:
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6',
                  '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self) -> str:
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __lt__(self, other):
        if self.suit < other.suit:
            return True
        if self.suit > other.suit:
            return False

        return self.rank < other.rank


class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        return self.cards.append(card)


print(Deck())
