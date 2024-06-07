
class CardHierarchy:
    def __init__(self, player_one_card, player_two_card):
        self.player_one_card = player_one_card
        self.player_two_card = player_two_card

    @property
    def player_one_card(self):
        return self._player_one_card

    @player_one_card.setter
    def player_one_card(self, value):
        self._player_one_card = value

    @property
    def player_two_card(self):
        return self.player_two_card

    @player_two_card.setter
    def player_two_card(self, value):
        self.player_two_card = value

    #def battle(self, player_one_card, player_two_card):


def main():
    pass


if __name__ == "__main__":
    main()
