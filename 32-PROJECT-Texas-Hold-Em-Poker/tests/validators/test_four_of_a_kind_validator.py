import unittest

from poker.card import Card
from poker.validators import FourOfAKindValidator

class FourOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):
        self.ace_of_clubs = Card("Ace", "Clubs")
        self.ace_of_diamonds = Card("Ace", "Diamonds")
        self.ace_of_hearts = Card("Ace", "Hearts")
        self.queen_of_spades = Card("Queen", "Spades")
        self.ace_of_spades = Card("Ace", "Spades")

        self.cards = [
            self.ace_of_clubs,
            self.ace_of_diamonds,
            self.ace_of_hearts,
            self.queen_of_spades,
            self.ace_of_spades
        ]
        
    
    def test_validates_that_four_cards_of_one_rank_are_present(self):
        validator = FourOfAKindValidator(self.cards)
        
        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_the_four_cards_with_the_same_rank(self):
        validator = FourOfAKindValidator(self.cards)
        
        self.assertEqual(
            validator.valid_cards(),
            [
                self.ace_of_clubs,
                self.ace_of_diamonds,
                self.ace_of_hearts,
                self.ace_of_spades
            ]
        )