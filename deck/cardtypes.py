from enum import Enum, unique


@unique
class Face(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

    def __str__(self):

        if self.value > 10:
            return str(self.name)
        return str(self.value)

    def __repr__(self):
        return str(self)


@unique
class Suit(Enum):
    HEARTS = 1 
    SPADES = 2
    DIAMONDS = 3
    CLUBS = 4

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self)
    