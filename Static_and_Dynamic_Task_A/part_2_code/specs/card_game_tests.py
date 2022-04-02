import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card = Card("hearts" , 14, "ace")
        self.card1 = Card("clubs" , 12, "king")
        self.card2 = Card("diamonds" ,13, "queen")

    def test_check_for_ace(self):
        self.assertEqual("ace" , self.card.symbol)

    def test_highest_card(self):
        self.assertEqual("ace" , self.card.symbol)

    def test_cards_total(self):
        self.assertEqual(39 , self.card.value)        