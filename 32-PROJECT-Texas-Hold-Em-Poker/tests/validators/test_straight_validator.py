import unittest

from poker.card import Card
from poker.validators import StraightValidator

class StraightValidatorTest(unittest.TestCase):
    def setUp(self):
        self.two_of_spades = Card("2", "Spades")
        self.six_of_hearts = Card("6", "Hearts")
        self.seven_of_diamonds = Card("7", "Diamonds")
        self.eight_of_spades = Card("8", "Spades")
        self.nine_of_clubs = Card("9", "Clubs")
        self.ten_of_clubs = Card("10", "Clubs")
        self.jack_of_hearts = Card("Jack", "Hearts")

        self.cards = [
            self.two_of_spades,
            self.six_of_hearts,
            self.seven_of_diamonds,
            self.eight_of_spades,
            self.nine_of_clubs,
            self.ten_of_clubs,
            self.jack_of_hearts
        ]

    def test_validates_that_there_are_five_cards_in_a_row(self):
        validator = StraightValidator(self.cards)
        
        self.assertEqual(
            validator.is_valid(),
            True
        )
    
    def test_returns_five_highest_cards_in_a_row(self):
        validator = StraightValidator(self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.seven_of_diamonds,
                self.eight_of_spades,
                self.nine_of_clubs,
                self.ten_of_clubs,
                self.jack_of_hearts
            ]
        )

    def test_does_not_deem_two_consecutive_cards_as_straight(self):
        two_of_hearts = Card("2", "Hearts")
        three_of_hearts = Card("3", "Hearts")
        
        cards = [
            two_of_hearts, three_of_hearts
        ]

        validator = StraightValidator(cards)

        self.assertEqual(validator.is_valid(), False)