import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.first_card = Card("club", 6)
        self.second_card = Card("heart", 1)
        self.third_card = Card("heart", 4)

        self.deck_of_cards = [self.first_card, self.second_card, self.third_card]
    
    def test_check_not_an_ace(self):
        expected = False
        actual = CardGame.check_for_ace(self, self.first_card)
        self.assertEqual(expected, actual)

    def test_check_for_ace(self):
        expected = True
        actual = CardGame.check_for_ace(self, self.second_card)
        self.assertEqual(expected, actual)   

    def test_highest_card(self):
        expected = self.first_card
        actual = CardGame.highest_card(self, self.first_card, self.second_card)
        self.assertEqual(expected, actual)   

    def test_total_of_cards(self):
        expected = "You have a total of 11"
        actual = CardGame.cards_total(self, self.deck_of_cards)
        self.assertEqual(expected, actual)   

