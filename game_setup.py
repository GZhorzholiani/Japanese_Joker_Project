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
        while True:
            chosen_trump_card = input(f"{trump_card_chooser} choose the trump card S, D, C, H, None: ").upper().strip()
            if chosen_trump_card in ["S", "D", "C", "H", "None"]:
                return chosen_trump_card


def main():
    gameplay = GameSetup(user_names(), total_cards_generator())
    card_distributor_player, trump_card_chooser_player = gameplay.card_distributor_and_trump_card_chooser()
    print(card_distributor_player)
    print(trump_card_chooser_player)
    print("*"*50)
    trump_card = gameplay.trump_card(trump_card_chooser_player)
    print(trump_card)


if __name__ == "__main__":
    main()
