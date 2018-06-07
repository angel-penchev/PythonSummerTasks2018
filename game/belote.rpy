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

        def __init__(self, deal = 3):

            # Constants that let us easily change where the game is
            # located.

            # Old Constants
            LEFT=140
            ROW_SPACING = 120
            CARD_XSPACING = 20
            CARD_YSPACING = 30

            # New Constants
            WIDTH = 1200
            HEIGHT = 900
            PLAYER_BOARDER_SPACING = 60
            PLAYER_CARDS_SPACING = 75

            # Store the parameters.
            self.deal = deal

            # Create the table, stock, and waste.
            self.table = t = Table(base="Assets/Cards/base.png", back="Assets/Cards/back.png")
            self.stock = t.stack(WIDTH / 2, HEIGHT / 2, xoff=0, yoff=0, click=False)


            # Create the card stock and shuffle it.
            for Rank in range(1, 8):            # Runs for 7, 8, 9, 10, Jacks (J), Queens (Q), King (K) & Aces (A)
                for Suit in range(0, 4):        # Runs for Clubs, Spades, Hearts and Diamounds
                    Value = (Suit, Rank)
                    t.card(Value, "Assets/Cards/%d.png" % self.card_num(Suit, Rank))    # Adds the card images
                    t.set_faceup(Value, False)  # Sets whether the card is facing Up or Down
                    self.stock.append(Value)    # Adds cards to the stock

            self.stock.shuffle()                # Shufles the cards in the stock


            self.PlayersCards = [];             # Defines the array containing the 4 players' cards
            self.PlayersStocks = [];            # Defines the array containing the current player stock

            for Player in range(0, 4):          # Runs for the 4 Players
                for CardsAmount in range(0, 8):
                    self.PlayersStocks.append(t.stack((WIDTH / 3.5) + PLAYER_CARDS_SPACING * CardsAmount, HEIGHT - ((PLAYER_BOARDER_SPACING + 40) * (Player + 1) - 40), xoff=0, yoff=0, drag=DRAG_TOP, drop=True))
                    self.PlayersCards.append(self.PlayersStocks[Player])



        # Start of Definitions Section

        def card_num(self, suit, rank):
            ranks = [ None, 1, 29, 25, 21, 17, 13, 9, 5 ]
            return suit + ranks[rank]


        def show(self):
            self.table.show()


        def hide(self):
            self.table.hide()


        def interact(self):

            evt = ui.interact()
            rv = False

            # Check the various events, and dispatch them to the methods
            # that handle them.
            if evt.type == "drag":
                if evt.drop_stack in self.tableau:
                    rv = self.tableau_drag(evt)

                elif evt.drop_stack in self.foundations:
                    rv = self.foundation_drag(evt)

            elif evt.type == "click":
                if evt.stack == self.stock:
                    rv = self.stock_click(evt)

            elif evt.type == "doubleclick":
                if (evt.stack in self.tableau) or (evt.stack is self.waste):
                    rv = self.tableau_doubleclick(evt)

            # Ensure that the bottom card in each tableau is faceup.
            for i in range(0, 7):
                if self.tableau[i]:
                    self.table.set_faceup(self.tableau[i][-1], True)

            # Check to see if any of the foundations has less than
            # 13 cards in it. If it does, return False. Otherwise,
            # return True.
            for i in self.foundations:
                if len(i) != 13:
                    return rv

            return "win"


        # Sets things as sensitive (or not).
        def set_sensitive(self, value):
            self.table.set_sensitive(value)


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
