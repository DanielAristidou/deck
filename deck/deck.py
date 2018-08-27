from .card import FaceCard
from .cardtypes import Face, Suit
from random import shuffle
from .hand import Hand


class Deck(object):

    def __init__(self, packs_of_cards=1):

        self.cards = [FaceCard(face, suit) for suit in Suit for face in Face for n in range(packs_of_cards)]

    def shuffle(self):
        shuffle(self.cards)

    def __len__(self):
        return len(self.cards)

    def draw(self):
        return self.cards.pop()

    def add(self, card, location):

        if not isinstance(card, FaceCard):
            raise TypeError("You cannot add a non card type to the deck. You passed object of type {}.".format(type(card)))

        self.cards.insert(location, card)

    def deal_hands(self, number_of_hands, number_of_cards):

        hands = [Hand([self.draw() for number in range(number_of_cards)]) for hand in range(number_of_hands)]

        return hands


