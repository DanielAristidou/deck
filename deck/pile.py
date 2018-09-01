from .card import FaceCard, JokerCard


class Pile(object):

    def __init__(self,cards=[]):

        self.__retrievable_cards = cards
        self.__cards = cards

    def add_to_pile(self,cards , top_of_pile=True, available_for_picking='EDGES'):

        for card in cards:
            if top_of_pile:
                self.__cards.append(card)
            else:
                self.__cards.insert(0,card)

        if available_for_picking == 'ALL':
            self.__retrievable_cards = cards
            return

        if available_for_picking == 'NONE':
            return

        if len(cards) > 1:
            self.__retrievable_cards = [cards[0], cards[-1]]
            return

        self.__retrievable_cards = [cards[0]]



    def take_card(self, face, suit):

        available_cards = self.__retrievable_cards
        wanted_card = FaceCard(face,suit)

        if wanted_card in available_cards:
            available_index = available_cards.index(wanted_card)
            pile_index = self.__cards.index(wanted_card)

        self.__retrievable_cards.pop(available_index)

        return self.__cards.pop(pile_index)

