class FiveCardRanksInARowValidator():
    @property
    def _collections_of_five_straight_cards_in_a_row(self):
        index = 0
        final_index = len(self.cards) - 1
        collections_of_five_straight_cards_in_a_row = []

        while index + 4 <= final_index:
            next_five_cards = self.cards[index:index + 5]
            next_five_rank_indices = [card.rank_index for card in next_five_cards]

            if self.every_element_increasing_by_one(next_five_rank_indices):
                collections_of_five_straight_cards_in_a_row.append(next_five_cards)

            index += 1
        return collections_of_five_straight_cards_in_a_row

    def every_element_increasing_by_one(self, rank_indices):
        starting_rank_index = rank_indices[0]
        last_rank_index = rank_indices[-1]
        return rank_indices == list(range(starting_rank_index, last_rank_index + 1))