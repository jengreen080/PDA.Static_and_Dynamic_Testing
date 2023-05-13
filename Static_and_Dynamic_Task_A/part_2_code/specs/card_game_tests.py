import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.first_card = Card("club", 6)
    
    def test_check_for_ace(self):
        expected = False
        actual = self.check_for_ace
        self.assertEqual(expected, actual)



