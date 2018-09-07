from .card import FaceCard
from .cardtypes import Face, Suit


class Hand(object):

    def __init__(self, cards):

        self.__cards = cards

    def retrieve_card(self, face, suit):
        if not isinstance(face, Face) and not isinstance(suit, Suit):
            raise TypeError("face and type must be of type Face and Type")

        index = self.__cards.index(FaceCard(face, suit))

        return self.__cards.pop(index)

    def retrieve_cards(self, cards):

        retrieved_cards = []

        for face, suit in cards:
            retrieved_cards.append(self.retrieve_card(face, suit))

        return retrieved_cards

    def add_card(self, card):

        if not isinstance(card, FaceCard):
            raise TypeError("card must be a FaceCard")

        self.__cards.append(card)

    def __repr__(self):
        return str(self.__cards)

    @property
    def face_values(self):
        return [card.face for card in self.__cards]

    @property
    def suit_values(self):
        return [card.suit for card in self.__cards]

    @property
    def cards_values(self):
        face = [card.face.value for card in self.__cards]
        suit = [card.suit.value for card in self.__cards]

        return list(zip(face, suit))

    @property
    def cards(self):
        return list(zip(self.face_values, self.suit_values))
