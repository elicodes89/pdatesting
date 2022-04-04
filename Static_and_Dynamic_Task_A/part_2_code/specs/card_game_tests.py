import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card = Card("hearts" , 14, "ace")
        self.card1 = Card("clubs" , 12, "king")
        self.card2 = Card("diamonds" ,13, "queen")
        self.cardgame = CardGame(0)

    def test_check_for_ace(self):
        self.assertEqual("ace" , self.card.symbol)

    def test_highest_card(self):
        CardGame.highest_card(self.card, self.card1)
        self.assertEqual("ace" , "ace")

    def test_cards_total(self):
        self.cardgame.cards.append(self.card)
        self.cardgame.cards.append(self.card1)
        self.cardgame.cards.append(self.card2)
        total = CardGame.cards_total(self.cardgame)
        self.assertEqual(39 , total)       