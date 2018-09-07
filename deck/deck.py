from .card import FaceCard, JokerCard
from .cardtypes import Face, Suit, Special
from random import shuffle
from .hand import Hand


class Deck(object):

    def __init__(self, packs_of_cards=1, number_of_jokers=2):

        self.__cards = [FaceCard(face, suit) for suit in Suit for face in Face for n in range(packs_of_cards)]

        for i in range(number_of_jokers):
            self.__cards.append(JokerCard())

        self.__initial_size = len(self.__cards)

    def shuffle(self):
        shuffle(self.__cards)

    def __len__(self):
        return len(self.__cards)

    def draw(self):
        return self.__cards.pop()

    def add(self, card, location):

        if not isinstance(card, FaceCard):
            raise TypeError("You cannot add a non card type to the deck. Passed object of type {}.".format(type(card)))

        self.__cards.insert(location, card)

    def deal_hands(self, number_of_hands, number_of_cards):

        hands = [Hand([self.draw() for _ in range(number_of_cards)]) for _ in range(number_of_hands)]

        return hands

    def has_card(self, **kwargs):

        face = kwargs.get('face', None)
        suit = kwargs.get('suit', None)

        if face != Special.JOKER:
            card = kwargs.get('card', FaceCard(face, suit))

        if face == Special.JOKER or suit == Special.JOKER:
            card = JokerCard()

        if card in self.__cards:
            return True

        return False

    @property
    def has_all_cards(self):
        return len(self.__cards) == self.__initial_size









