import unittest

from poker.card import Card
from poker.validators import TwoPairValidator

class TwoPairValidatorTest(unittest.TestCase):
    def setUp(self):
        self.four_of_hearts = Card("4", "Hearts")
        self.queen_of_diamonds = Card("Queen", "Diamonds")
        self.queen_of_spades = Card("Queen", "Spades")
        self.ace_of_clubs = Card("Ace", "Clubs")
        self.ace_of_spades = Card("Ace", "Spades") 

        self.cards = [
            self.four_of_hearts,
            self.queen_of_diamonds,
            self.queen_of_spades,
            self.ace_of_clubs,
            self.ace_of_spades
        ]


    def test_validates_that_cards_have_at_least_two_pairs_of_same_rank(self):
        validator = TwoPairValidator(self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_collection_of_cards_that_have_pairs(self):
        validator = TwoPairValidator(self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.queen_of_diamonds, 
                self.queen_of_spades, 
                self.ace_of_clubs, 
                self.ace_of_spades
            ]
        )