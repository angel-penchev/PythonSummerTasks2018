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
                                                # Creates a table and defines the base and back images of the stocks and card
            self.MainStock = t.stack(WIDTH / 2, HEIGHT / 2, xoff = 0, yoff = 0, base = None, click = False, drag = DRAG_NONE, drop = False, hidden = False)


            # Create the card stock and shuffle it.
            for Rank in range(0, 8):            # Runs for 7, 8, 9, 10, Jacks (J), Queens (Q), King (K) & Aces (A)
                for Suit in range(0, 4):        # Runs for Clubs, Spades, Hearts and Diamounds
                    Value = (Suit, Rank)
                    t.card(Value, "Assets/Cards/%d.png" % self.CardNumber(Suit, Rank))
                                                # Associates the image with a given card
                    t.set_faceup(Value, True)   # Sets whether the card is facing Up or Down
                    self.MainStock.append(Value)# Adds cards to the stock

            self.MainStock.shuffle()                # Shufles the cards in the stock


            # Creates the players' card stocks
            self.PlayerStocks = [];              # Defines the array containing the 4 players' card stocks
            for Player in range (0, 4):          # Runs for the 4 Players
                    self.PlayerStocks.append(t.stack((WIDTH / 3.5), HEIGHT - ((PLAYER_BOARDER_SPACING + 40) * (Player + 1) - 40), xoff = 75, yoff = 0, drag = DRAG_TOP, drop = True))
                                                # Creates a player stock with position parameters


            # Deals the initial 3 cards to all the players
            for Player in range (0, 4):
                for CardsAmount in range (0, 3):
                    current = self.MainStock.deal()
                    self.PlayerStocks[Player].append(current)

            # Deals the following 2 cards to all the players
            for Player in range (0, 4):
                for CardsAmount in range (0, 3):
                    current = self.MainStock.deal()
                    self.PlayerStocks[Player].append(current)



            # TODO: Create trump selection game part here!



            # Deals the last 3 cards to all the players
            for Player in range (0, 4):
                for CardsAmount in range (0, 2):
                    current = self.MainStock.deal()
                    self.PlayerStocks[Player].append(current)

        # Start of Definitions Section

        # CardNumber - Used for generating the file name of a given card
        def CardNumber(self, Suit, rank):
            ranks = [29, 25, 21, 17, 13, 9, 5, 1]
            return Suit + ranks[rank]


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
                if evt.stack == self.MainStock:
                    rv = self.MainStock_click(evt)

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
            Suit, rank = c
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
                "Diamonds" ][Suit]

        # End of Definitions Section
