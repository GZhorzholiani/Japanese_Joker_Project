import random
from players import user_names
from total_cards_generator import total_cards_generator


class GameSetup:
    def __init__(self, players, total_cards):
        self.players = players
        self.total_cards = total_cards

    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, value):
        self._players = value

    @property
    def total_cards(self):
        return self._total_cards

    @total_cards.setter
    def total_cards(self, value):
        self._total_cards = value

    def card_distributor_and_trump_card_chooser(self):
        card_distributor = random.choice(self.players)
        self.players.remove(card_distributor)
        trump_card_chooser = self.players[0]
        return card_distributor, trump_card_chooser

    @staticmethod
    def trump_card(trump_card_chooser):
        card_suits = ["C", "S", "H", "D", "NONE"]
        trump_card_visual = {"C": '\x1b[107m\x1b[30m♣\x1b[0m', "S": '\x1b[107m\x1b[30m♠\x1b[0m',
                             "H": '\x1b[107m\x1b[31m♥\x1b[0m', "D": '\x1b[107m\x1b[31m♦\x1b[0m'}
        while True:
            chosen_trump_card = input(f"{trump_card_chooser} choose the trump card, type C for {trump_card_visual['C']}, S for {trump_card_visual['S']}, "
                                      f"H for {trump_card_visual['H']}, D for {trump_card_visual['D']} or None: ").upper().strip()
            if chosen_trump_card in card_suits:
                card_suits.remove(chosen_trump_card)
                if chosen_trump_card != "NONE":
                    card_suits.remove("NONE")
                return chosen_trump_card, card_suits, trump_card_visual

    @staticmethod
    def trump_card_effect(total_cards: dict, chosen_trump_card):
        if chosen_trump_card != "NONE":
            for card in total_cards.keys():
                if card[0] == chosen_trump_card:
                    total_cards[card] += 50
        return total_cards


def main():
    total_cards = list(total_cards_generator().keys())
    gameplay = GameSetup(user_names(), total_cards)
    card_distributor_player, trump_card_chooser_player = gameplay.card_distributor_and_trump_card_chooser()
    print(card_distributor_player)
    print(trump_card_chooser_player)
    print("*"*50)
    trump_card, card_suits, trump_card_visual = gameplay.trump_card(trump_card_chooser_player)
    print(trump_card)
    trump_total_cards = gameplay.trump_card_effect(total_cards_generator(), trump_card)
    print(trump_total_cards)


if __name__ == "__main__":
    main()
