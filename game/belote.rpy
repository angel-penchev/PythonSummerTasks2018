# belote.rpy - Belote Script

init python:

    class Belote(object):

        # We represent a card as a (suit, rank) tuple. The suit is one of the
        # following four constants, while the rank is 1 for ace, 2 for 2,
        # ..., 10 for 10, 11 for jack, 12 for queen, 13 for king.
        CLUB = 0
        SPADE = 1
        HEART = 2
        DIAMOND = 3

        def __init__(self, deal=3):

            # Constants that let us easily change where the game is
            # located.
            LEFT = 140
            TOP = 58
            COL_SPACING = 75
            ROW_SPACING = 200
            CARD_XSPACING = 20
            CARD_YSPACING = 30

            # Store the parameters.
            self.deal = deal

            return False

        def card_name(self, c):
            suit, rank = c

            return  [
                "INVALID",
                "Ace",
                "Two",
                "Three",
                "four",
                "Five",
                "Six",
                "Seven",
                "Eight",
                "Nine",
                "Ten",
                "Jack",
                "Queen",
                "King" ][rank] + " of " + [
                "Clubs",
                "Spades",
                "Hearts",
                "Diamonds" ][suit]
