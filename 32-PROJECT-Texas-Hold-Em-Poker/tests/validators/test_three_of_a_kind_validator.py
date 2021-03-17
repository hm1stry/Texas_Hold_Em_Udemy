import unittest

from poker.card import Card
from poker.validators import ThreeOfAKindValidator

class ThreeOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):
        self.four_of_hearts = Card("4", "Hearts")
        self.queen_of_spades = Card("Queen", "Spades")
        self.ace_of_clubs = Card("Ace", "Clubs")
        self.ace_of_diamonds = Card("Ace", "Diamonds")
        self.ace_of_spades = Card("Ace", "Spades")

        self.cards = [
            self.four_of_hearts,
            self.queen_of_spades,
            self.ace_of_clubs,
            self.ace_of_diamonds,
            self.ace_of_spades
        ]

    def test_validates_that_cards_have_exactly_three_of_the_same_rank(self):
        validator = ThreeOfAKindValidator(self.cards)

        self.assertEqual(
            validator.is_valid(), 
            True
        )

    def test_returns_three_of_a_kind_cards_from_card_collection(self):
        validator = ThreeOfAKindValidator(self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.ace_of_clubs,
                self.ace_of_diamonds,
                self.ace_of_spades
            ]
        )
    