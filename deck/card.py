from .cardtypes import Suit, Face


class FaceCard(object):

    def __init__(self, face, suit):

        if not isinstance(face, Face):
            raise TypeError("face is not of type Face. you passed type {}.".format(type(face)))

        if not isinstance(suit, Suit):
            raise TypeError("suit is not of type suit. you passed type {}.".format(type(face)))

        self.face = face
        self.suit = suit

    def same_face(self, face):
        return self.face.value == face

    def same_suit(self, suit):
        return self.suit.value == suit

    def __eq__(self, other):

        if isinstance(other, FaceCard):
            return self.same_face(other.face.value) and self.same_suit(other.suit.value)
        raise TypeError("{} is not of type Card".format(other))

    def __bool__(self):
        return False

    def __repr__(self):
        rep = str(self.face) + " of " + str(self.suit)
        return str(rep)