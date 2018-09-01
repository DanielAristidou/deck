from .cardtypes import Suit, Face, Special


class FaceCard(object):

    def __init__(self, face, suit):

        if not isinstance(face, Face):
            raise TypeError("face is not of type Face. you passed type {}.".format(type(face)))

        if not isinstance(suit, Suit):
            raise TypeError("suit is not of type suit. you passed type {}.".format(type(face)))

        self.__face = face
        self.__suit = suit

    @property
    def face(self):
        return self.__face

    @property
    def suit(self):
        return self.__suit

    def same_face(self, face):
        return self.__face.value == face

    def same_suit(self, suit):
        return self.__suit.value == suit

    def __eq__(self, other):

        if isinstance(other, JokerCard):
            return True

        if isinstance(other, FaceCard):
            return self.same_face(other.__face.value) and self.same_suit(other.__suit.value)
        raise TypeError("{} is not of type Card".format(other))

    def __repr__(self):
        rep = str(self.__face) + " of " + str(self.__suit)
        return str(rep)


class JokerCard(object):

    def __init__(self):

        self.__face = Special.JOKER
        self.__suit = Special.JOKER

    @property
    def face(self):
        return self.__face

    @property
    def suit(self):
        return self.__suit

    def same_face(self, face):
        return self.__face.value == face

    def same_suit(self, suit):
        return self.__suit.value == suit

    def __eq__(self,other):

        return True

    def __repr__(self):
        return str(self.__face)
