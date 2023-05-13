import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.first_card = Card("club", 6)
        self.second_card = Card("heart", 1)
    
    def test_check_not_an_ace(self):
        expected = False
        actual = CardGame.check_for_ace(self, self.first_card)
        self.assertEqual(expected, actual)

    def test_check_for_ace(self):
        expected = True
        actual = CardGame.check_for_ace(self, self.second_card)
        self.assertEqual(expected, actual)   



