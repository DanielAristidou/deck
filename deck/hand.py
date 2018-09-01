from .card import FaceCard
from .cardtypes import Face, Suit


class Hand(object):

    def __init__(self, cards):

        self.cards = cards

    def retrieve_card(self, face, suit):
        if not isinstance(face, Face) and not isinstance(suit, Suit):
            raise TypeError("face and type must be of type Face and Type")

        index = self.cards.index(FaceCard(face, suit))

        return self.cards.pop(index)

    def retrieve_cards(self, cards):

        retrieved_cards = []

        for face, suit in cards:
            retrieved_cards.append(self.retrieve_card(face, suit))

        return retrieved_cards

    def add_card(self, card):

        if not isinstance(card, FaceCard):
            raise TypeError("card must be a FaceCard")

        self.cards.append(card)

    def __repr__(self):
        return str(self.cards)

    def face_values(self):
        return [card.face for card in self.cards]

    def suit_values(self):
        return [card.suit for card in self.cards]
